from collections import defaultdict 
import numpy as np
import json
import os

import onnx
from onnx.defs import OpSchema, ONNX_DOMAIN, ONNX_ML_DOMAIN
from onnx.backend.test.case import collect_snippets
from onnx.backend.sample.ops import collect_sample_implementations


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

ML = root + '/ml'
NN = root + '/nn'

def _attr_type(attr):
    assert isinstance(attr, OpSchema.AttrType)
    a = str(attr)
    a = a[a.rfind('.') + 1:].lower()
    if a[-1] == 's' or a == 'graph' or a == 'tensor':
        a = 'list'
    if a == 'string':
        a = 'str'
    return a


def _schema(f, schema):
    doc = ''
    file = '\n'.join(['import numpy as np', 'from __future__ import absolute_import', 'from __future__ import division'])
    

    for n_schema in schema:
        name = n_schema.name
        file += '\n\nclass {0}_{1}:\n'.format(name, n_schema.since_version)


        if n_schema.doc:
            doc = '\n' + '\n'.join('  ' + line for line in n_schema.doc.lstrip().splitlines()) + '\n'
            
        if n_schema.support_level == OpSchema.SupportType.EXPERIMENTAL:
            return
        if n_schema.deprecated:
            return

        attributes = []
        inputs = []
        outputs = []

        if n_schema.attributes:
            for _, attr in sorted(n_schema.attributes.items()):
                file += '\n\t' + attr.name + ' = m_' + _attr_type(attr.type) + '()'
                attributes.append((attr.name, _attr_type(attr.type)))
        file += '\n'
        if n_schema.inputs:
            for input in n_schema.inputs:
                inputs.append(input.name)
        if n_schema.outputs:
            for output in n_schema.outputs:
                outputs.append(output.name)
        #init
        file += '\tdef __init__(self, _name: str, _tensor: dict{0}):'.format(''.join(', {0}: {1}'.format(i, j) for i, j in attributes))
        file += '\n\t\tself.name = _name'
        file += '\n\t\tself.tensor = _tensor'
        file += ''.join('\n\t\tself.m_{0} = {0}'.format(i) for i,j in attributes)

        #call
        file += '\n\n\tdef __call__(self{0}):'.format(''.join(', {0}: str'.format(i) for i in inputs))
        file += '\n\t\tinput = (' + ', '.join('self.tensor[{0}]'.format(i) for i in inputs) + ')'
        file += '\n\t\treturn {0}'. format(', '.join('self.tensor[{0}]'.format(i) for i in outputs))
        

        file += '\n'

        if n_schema.has_function:
            print(n_schema.name)

    f.write(file)

def build():
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
    
    initf.write('from . import *')
    initf2.write("from . import *")

    schemas = onnx.defs.get_all_schemas()
    func_ops = onnx.defs.get_function_ops()
    
    index = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for schema in onnx.defs.get_all_schemas_with_history():
        index[schema.domain][int(schema.support_level)][schema.name].append(schema)
    
    for support_level in index['ai.onnx.ml']:
        ml_schemas = index['ai.onnx.ml'][support_level]
        for ml_schema in ml_schemas:
            f = open(ML + "/{0}.py".format(ml_schema), 'w')
            schema=ml_schemas[ml_schema]
            _schema(f, schema)
            
    for support_level in index['']:
        nn_schemas = index[''][support_level]
        for nn_schema in nn_schemas:
            f = open(NN + "/{0}.py".format(nn_schema), 'w')
            schema=nn_schemas[nn_schema]
            _schema(f, schema)

if(__name__=='__main__'):
    build()