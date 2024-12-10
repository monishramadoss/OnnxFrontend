import nn 
import ml

import onnx
from onnx import numpy_helper
from onnx import helper, shape_inference
from onnx import AttributeProto, TensorProto, GraphProto
from onnx.helper import make_tensor_value_info, make_graph, make_model, get_attribute_value
from onnx.mapping import NP_TYPE_TO_TENSOR_TYPE, TENSOR_TYPE_TO_NP_TYPE
import onnx.utils

import numpy as np
import os
import site
import sys
import inspect

MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')

def package_contents(package_name):
    file, pathname, _ = imp.find_module(package_name)
    if file:
        raise ImportError('Not a package: %r', package_name)
    return set([os.path.splitext(module)[0] for module in os.listdir(pathname) if module.endswith(MODULE_EXTENSIONS)])

def np_dtype_to_tensor_type_name(data_type):
    return TensorProto.DataType.Name(NP_TYPE_TO_TENSOR_TYPE[data_type])

def np_dtype_to_tensor_type(data_type):
    return NP_TYPE_TO_TENSOR_TYPE[data_type]

class onnx_graph:
    def __init__(self, filename):
        self.filename = filename
        model = onnx.load(filename)
        self.prepare(model)
     
    def prepare(self, model):
        model = shape_inference.infer_shapes(model)
        self.graph = model.graph
        self.value_info = self.graph.value_info

        self.tensors = {}
        self.nodes = {}
        self.tensor_data = {'':0}
        self.layers = {}

        for vi in self.graph.input:
            self.tensors[vi.name] = vi
            self.tensor_data[vi.name] = np.zeros([i.dim_value for i in vi.type.tensor_type.shape.dim]).astype(np.float32)
        for vi in self.graph.output:
            self.tensors[vi.name] = vi
            self.tensor_data[vi.name] = np.zeros([i.dim_value for i in vi.type.tensor_type.shape.dim]).astype(np.float32)
        for vi in self.value_info:
            self.tensors[vi.name] = vi
            self.tensor_data[vi.name] = np.zeros([i.dim_value for i in vi.type.tensor_type.shape.dim]).astype(np.float32)
        for init in self.graph.initializer:
            self.tensor_data[init.name] = numpy_helper.to_array(init)
                    
        version = model.opset_import[0].version
        ops = set()
        for node in self.graph.node:
            if node.op_type in nn.layer:
                ops.add(node.op_type)
                layer = nn.layer[node.op_type]
            if node.op_type in ml.layer:
                layer = ml.layer[node.op_type]
                print('ML OP:', node.op_type)
            attr = dict([('_name', node.name), ('_tensor', self.tensor_data)] + [(a.name, get_attribute_value(a)) for a in node.attribute])
            for i, l in sorted(layer.items(), key=lambda x: x[0], reverse=True):
                if(i <= version):
                    self.layers[node.name] = l(**attr)
                    break
        print("USED OPS :", ops)

        for node in self.graph.node:
            i = node.input
            o = node.output

            if(node.op_type not in ['Scan']):
                self.layers[node.name].output(*o)
            else:
                self.layers[node.name].output(o)
            if(node.op_type not in ['Concat', 'Sum', 'Scan', 'Mean']):
                self.layers[node.name](*i)
            else:
                self.layers[node.name](i)
        
        print()

def get_onnx_proto():
    """
    Finds the ONNX directory within the site-packages and generates the ONNX protobuf files 
    if the directory does not exist locally. Utilizes the 'onnx.gen_proto' module to perform 
    the generation and outputs the files to a specified directory.
    """
    import os
    import site
    import subprocess
    site_packages_dir = site.getsitepackages()[0]
    print(site.getsitepackages())
    onnx_dir = os.path.join(site_packages_dir, 'onnx')
    if not os.path.exists(onnx_dir):
        for pkg_dir in site.getsitepackages():
            for root, dirs, files in os.walk(pkg_dir):
                if 'onnx' in dirs:
                    onnx_dir = os.path.join(root, 'onnx')
                    site_packages_dir= pkg_dir
                    break

        if(not os.path.exists('./onnx')):
            subprocess.Popen('python -m onnx.gen_proto -m -o ./onnx')
        for root, dirs, files in os.walk('./onnx'):
            for file in files:
                print(root)
                if file.endswith('.proto'):
                    print(f'protoc --cpp_out=cpps --proto_path={root} {os.path.join(root, file)}')
