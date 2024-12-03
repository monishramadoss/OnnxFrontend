from collections import defaultdict 
import numpy as np
import shutil
import os

import onnx
from onnx.defs import OpSchema


python_class_str = """

class {norm}:
    name = None
{python_variables}
    #parameters
{python_parameters}
    input_params = [{python_inputs_func}]
    output_params = [{python_outputs_func}]
    attribute_params = [{python_attribute_func}]
  
    def __init__(self, name, **kwargs):
        self.name = name
        self.__dict__.update(kwargs)
       
    def output_shape(self):
        return tensors[self.__dict__[self.input_params[0]]].shape 

    def __call__(self, *args):
        for i, x in enumerate(args):
            self.__dict__[self.input_params[i]] = x           
        return self

    def output(self, *args):
        for i, x in enumerate(args):
            self.__dict__[self.output_params[i]] = x            
            if(x not in tensors.keys()):     
                tensors[x] =  np.zeros(self.output_shape())
        return self

    def test(self):
        {python_self_output}
        
       

layer_map['{norm}'] = {norm}

""".format_map
root = '.'

def _attr_type(attr):
    assert isinstance(attr, OpSchema.AttrType)
    a = str(attr)
    a = a[a.rfind('.') + 1:].lower()
    if a[-1] == 's' or a == 'graph' or a == 'tensor':
        a = 'list'
    if a == 'string':
        a = 'str'
    return a


def _python_schema(f, schema):
    doc = ''
    file = '\n'.join(['from __future__ import absolute_import', 'from __future__ import division', 'import numpy as np',])
    

    for n_schema in schema:
        name = n_schema.name
        file += '\n\nclass {0}_{1}:\n'.format(name, n_schema.since_version)

        if n_schema.doc:
            doc = '\n' + '\n'.join('  ' + line for line in n_schema.doc.lstrip().splitlines()) + '\n'
            
        if n_schema.support_level != OpSchema.SupportType.EXPERIMENTAL or not n_schema.deprecated:
            attributes = []
            inputs = []
            outputs = []

            if n_schema.attributes:
                for _, attr in sorted(n_schema.attributes.items()):
                    file += '\n\tm_' + attr.name + ' = ' + _attr_type(attr.type) + '()'
                    attributes.append((attr.name, _attr_type(attr.type)))
            file += '\n'
            if n_schema.inputs:
                for input in n_schema.inputs:
                    inputs.append(input.name)
            if n_schema.outputs:
                for output in n_schema.outputs:
                    outputs.append(output.name)
            #init
            file += '\tdef __init__(self, _name: str, _tensor: dict{0}):'.format(''.join(', {0}={1}()'.format(i, j) for i, j in attributes))
            file += '\n\t\tself.name = _name'
            file += '\n\t\tself.tensor = _tensor'
            file += ''.join('\n\t\tself.m_{0} = {0}'.format(i) for i,j in attributes)

            #output
            file += '\n\n\tdef output(self{0}):'.format(''.join(', {0}=str()'.format(i) for i in outputs))
            file += '\n\t\t' + '\n\t\t'.join('self.m_{0} = {0}'.format(i) for i in outputs) + '\n'

            #call
            file += '\n\n\tdef __call__(self{0}):'.format(''.join(', {0}=str()'.format(i) for i in inputs))
            file += '\n\t\t' + '\n\t\t'.join('self.m_{0} = {0}'.format(i) for i in inputs) + '\n'
            file += '\n\t\treturn ({0})'. format(', '.join('self.tensor[self.m_{0}]'.format(i) for i in outputs))   
            file += '\n'

            if n_schema.has_function:
                print(n_schema.name)
                file += "\n\n\tdef function(self, layer):"
                for k, i in enumerate(n_schema.function_body.node):
                    # if(i.op_type == 'Constant'):
                    #     file += '\n\t\tself.tensor["{0}"] = 0'.format(i.output[0])                    
                    # else:
                        file += '\n\t\tl{0} = layer["{1}"]('.format(k, i.op_type)
                        for j in i.attribute:
                            file += '{0}={1}, '.format(j.name, j.s)
                            if(j.ref_attr_name != ''):
                                file += '{0}=self.m_{0}, '.format(j.ref_attr_name)
                        file += ')'
                        
                        inputs = ['self.tensor["{0}"]'.format(i) for i in i.input]
                        file += '\n\t\tself.tensor["{0}"] = l{1}( '.format(i.output[0], k)
                        
                        if(len(i.input) > 0): 
                            file += 'self.tensor["{0}"]'.format(i.input[0])
                            for j in i.input[1:]:
                                file += ', self.tensor["{0}"]'.format(j)
                        file += ')'
                file += '\n'

                context_dependent = n_schema.has_context_dependent_function 
                data_propagation = n_schema.has_data_propagation_function
                shape_inference = n_schema.has_type_and_shape_inference_function  

    f.write(file.replace('...',''))

def build_python(root, regen=False):
    ML = root + '/ml'
    NN = root + '/nn'

    if not regen and os.path.isdir(ML) and os.path.isdir(NN):
        return
   
    if not os.path.isdir(ML):
        os.mkdir(ML)
    else:        
        map(os.unlink, (os.path.join(ML,f) for f in os.listdir(ML)) )
        
    if not os.path.isdir(NN):
        os.mkdir(NN)
    else:
        map(os.unlink, (os.math.join(NN,f) for f in os.listdir(NN)) )
    
    initf = open(ML + '/__init__.py', 'w')
    initf2 = open(NN + '/__init__.py', 'w')
    
    initf.write('from . import *\nlayer={}\n')
    initf2.write("from . import *\nlayer={}\n")

    func_ops = onnx.defs.get_function_ops()
    func_ops = {op.name: op for op in func_ops}
    print(func_ops.keys())
    index = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for schema in onnx.defs.get_all_schemas_with_history():
        index[schema.domain][int(schema.support_level)][schema.name].append(schema)
    for support_level in index['ai.onnx.ml']:
        ml_schemas = index['ai.onnx.ml'][support_level]
        for ml_schema in ml_schemas:
            f = open(ML + "/{0}.py".format(ml_schema), 'w')
            schema=ml_schemas[ml_schema]

            version = list()
            for i in schema:
                version.append(str(i.since_version))
                depricated = i.deprecated
            if(not depricated):
                initf.write("\nfrom . import {0}\nlayer['{0}'] = {{{1}}}".format(schema[0].name, ', '.join('{1}: {0}.{0}_{1}'.format(schema[0].name, v) for v in version)))
            
            _python_schema(f, schema)
            
    for support_level in index['']:
        nn_schemas = index[''][support_level]
        for nn_schema in nn_schemas:
            f = open(NN + "/{0}.py".format(nn_schema), 'w')
            schema=nn_schemas[nn_schema]

            version = list()
            depricated = False
            for i in schema:
                version.append(str(i.since_version))
                depricated = i.deprecated
            if(not depricated):
                initf2.write("\nfrom . import {0}\nlayer['{0}'] = {{{1}}}".format(schema[0].name, ', '.join('{1}: {0}.{0}_{1}'.format(schema[0].name, v) for v in version)))
            _python_schema(f, schema)

def _c_type(t):
    if(t == 1):
        return "int"
    if(t == 2):
        return "float"
    if(t == 3):
        return "std::string"
    if(t == 4):
        return "tensor"
    if(t == 5):
        return "Operator"
    if(t == 6):
        return "std::vector<float>"
    if(t == 7):
        return "std::vector<int>"
    if(t == 8):
        return "std::vector<std::string>"
    if(t == 9):
        return "std::vector<tensor>"
    if(t == 10):
        return "std::vector<Operator>"
    if(t == 11):
        return "sparse_tensor"
    if(t == 12):
        return "std::vector<sparse_tensor>"
    if(t == 13):
        return "// tensor"
    if(t == 14):
        return "// std::vector<tensor>"

def _c_schema(h, c, schema, nodes):
    header = ''
    cpp = ''
    header_file_path = os.path.realpath(h.name)
    for n_schema in schema:
        name = n_schema.name
        header += "\n\n/* {0} \n*/".format(n_schema.doc)
        if(n_schema.deprecated):
            continue

        header += '\ntypedef struct {0}_{1}_inputs'.format(name, n_schema.since_version) + " {"
        for i in n_schema.inputs:
            if i.option.value == 0:
                header += "\n\ttensor {0};".format(i.name)
            elif i.option.value == 1:
                header += "\n\tstd::optional<tensor> {0};".format(i.name)
            else:
                header += "\n\tstd::vector<tensor> {0};".format(i.name)

        header += "\n}" + " {0}_{1}_inputs;".format(name, n_schema.since_version)
        header += '\n\ntypedef struct {0}_{1}_outputs'.format(name, n_schema.since_version) + " {"
        for i in n_schema.outputs:
            if i.option.value == 0:
                header += "\n\ttensor {0};".format(i.name)
            elif i.option.value == 1:
                header += "\n\tstd::optional<tensor> {0};".format(i.name)
            else:
                header += "\n\tstd::vector<tensor> {0};".format(i.name)
        header += "\n}" + " {0}_{1}_outputs;".format(name, n_schema.since_version)

        if len(n_schema.attributes) > 0:    
            header += '\n\ntypedef struct {0}_{1}_attributes'.format(name, n_schema.since_version) + " {"
            for k, v in n_schema.attributes.items():
                type = _c_type(v.type.value)
                
                header += "\n\t {0} {1};".format(type, v.name)
            header += "\n}" + " {0}_{1}_attributes;".format(name, n_schema.since_version)

        header += "\n\ntypedef struct {0}_{1} : public Operator ".format(name, n_schema.since_version) + "{"
        header += "\n\t{0}_{1}_inputs inputs;".format(name, n_schema.since_version)
        header += "\n\t{0}_{1}_outputs outputs;".format(name, n_schema.since_version)
        if len(n_schema.attributes) > 0:
            header += "\n\t{0}_{1}_attributes attributes;".format(name, n_schema.since_version)
        header += "\n}" + " {0}_{1};".format(name, n_schema.since_version)
        header += '\n\nvoid function({0}_{1} fn); '.format(name, n_schema.since_version)
        cpp += '\n\nvoid function({0}_{1} fn)'.format(name, n_schema.since_version) + " {"
        if n_schema.has_function or n_schema.has_context_dependent_function:
            print(name, "----")

            k = 0
            
            for _, i in n_schema.attributes.items():
                cpp += '\n\t{0} {1} = fn.attributes.{1};'.format(_c_type(i.type), i.name)
            for i in n_schema.inputs:
                cpp += '\n\ttensor {0} = fn.inputs.{0};'.format(i.name)            
            cpp += '\n'

            for k, i in enumerate(n_schema.function_body.node):    
                op_version = onnx.defs.get_schema(i.op_type).since_version            
                cpp += '\n\t{0}_{1} l{2};'.format(i.op_type,  op_version, k)
            cpp += '\n'
            k = 0
            if(len(n_schema.function_body.node) > 0):
                node_0 = n_schema.function_body.node[0]
                for i in node_0.attribute:                    
                    cpp += '\n\tl{0}.attributes.{1} = {2};'.format(k, i.name, i.ref_attr_name)       
                for i in node_0.input:
                    cpp += '\n\tl{0}.inputs.{1} = {1};'.format(k, i)
                for i in node_0.output:
                    cpp += '\n\t{2} = l{0}.outputs.{1};'.format(k, i, i)       

                for k, j in enumerate(n_schema.function_body.node[1:-1]): 
                    for i in j.attribute:     
                        cpp += '\n\tl{0}.attributes.{1} = {2};'.format(k, i.name, i.ref_attr_name)       
                    for i in j.input:
                        cpp += '\n\tl{0}.inputs.{1} = {2};'.format(k, i, i)
                    for i in j.output:
                        cpp += '\n\t{2} = l{0}.outputs.{1};'.format(k, i, i)       

                for o in n_schema.outputs:
                    cpp += '\n\tfn.outputs.{0} = l{1}.outputs.{2};'.format(o.name, k, o.name)

                cpp += '\n'

            for k, i in enumerate(n_schema.function_body.node):
                cpp += '\n\tfunction(l{0});'.format(k)
            cpp += '\n'

            cpp += '\n'
        cpp += ' }'

    c.write(cpp.replace('...', ''))
    h.write(header.replace('...', ''))
    

def build_c(root, regen=False):
    C = root 
    if not regen and os.path.isdir(C):
        return
    
    if not os.path.isdir(C):
        os.mkdir(C)
    if not os.path.isdir(os.path.join(C, 'ml')):
        os.mkdir(os.path.join(C, 'ml'))
    if not os.path.isdir(os.path.join(C, 'nn')):
        os.mkdir(os.path.join(C, 'nn'))
    
    map(os.unlink, (os.path.join(os.path.join(C, 'ml'),f) for f in os.listdir(os.path.join(C, 'ml'))) )
    map(os.unlink, (os.path.join(os.path.join(C, 'nn'),f) for f in os.listdir(os.path.join(C, 'nn'))) )
    
    nnfh = open(C + '/nn.h', 'w')    
    nnfh.write('#include "tensor.h"\n')
    nnfc = open(C + '/nn.c', 'w')
    nnfc.write('#include "nn.h"\n')
 
    mlfh = open(C + '/ml.h', 'w')
    mlfh.write('#include "tensor.h"\n')
    mlfc = open(C + '/ml.c', 'w')
    mlfc.write('#include "ml.h"\n')
    
    CMakeFile = open(C + '/CMakeLists.txt', 'w')
    CMakeFile.write('cmake_minimum_required(VERSION 3.10)\n')
    CMakeFile.write('project(OnnxCPP)\n')
    CMakeFile.write('set(CMAKE_CXX_STANDARD 17)\n')
    
    CMakeFile.write('add_library(OnnxCPP SHARED nn.c ml.c)\n')


    func_ops = onnx.defs.get_function_ops()
    nodes = {}
    index = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for schema in onnx.defs.get_all_schemas_with_history():
        index[schema.domain][int(schema.support_level)][schema.name].append(schema)
        
    for support_level in index['ai.onnx.ml']:
        ml_schemas = index['ai.onnx.ml'][support_level]
        for ml_schema in ml_schemas:
            schema=ml_schemas[ml_schema]
            mlfh.write('#include "./ml/{0}.h"\n'.format(schema[0].name))
            node_h = open(os.path.join(C, 'ml', schema[0].name + '.h'), 'w')
            _c_schema(node_h, mlfc, schema, nodes)

    nodes = {}
    for support_level in index['']:
        nn_schemas = index[''][support_level]
        for nn_schema in nn_schemas:
            schema=nn_schemas[nn_schema]
            nnfh.write('#include "./nn/{0}.h"\n'.format(schema[0].name))
            node_h = open(os.path.join(C, 'nn', schema[0].name + '.h'), 'w')    
            _c_schema(node_h, nnfc, schema, nodes)  
        
    mlfc.close()
    nnfc.close()
    mlfh.close()
    nnfh.close()



    


def build(code_type, root, regen=False):
    if not os.path.isdir(root + '/out'):
        os.mkdir(root + '/out')
    if code_type == 'python':
        build_python(root + '/out', regen)
    elif code_type == 'c':
        build_c(root + '/out', regen)
    else:
        raise ValueError('Unknown code type: {}'.format(code_type))
    