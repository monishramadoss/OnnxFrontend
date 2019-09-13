import nn 
import ml

import onnx
from onnx import numpy_helper
from onnx import helper, shape_inference
from onnx import AttributeProto, TensorProto, GraphProto
from onnx.helper import make_tensor_value_info, make_graph, make_model
from onnx.mapping import NP_TYPE_TO_TENSOR_TYPE, TENSOR_TYPE_TO_NP_TYPE
import onnx.utils

import numpy as np
import os
import inspect
import sys
#import onnxruntime as ort

def np_dtype_to_tensor_type_name(data_type):
    return TensorProto.DataType.Name(NP_TYPE_TO_TENSOR_TYPE[data_type])

def np_dtype_to_tensor_type(data_type):
    return NP_TYPE_TO_TENSOR_TYPE[data_type]

class onnx_graph:
    def __init__(self, filename):
        map(os.unlink, (os.path.join('./model',f) for f in os.listdir('./model')) )
        self.filename = filename
        model = onnx.load(filename)
        model = onnx.utils.polish_model(model)
        self.graph = model.graph
        self.value_info = self.graph.value_info

        self.tensors = {}
        self.nodes = {}
        self.tensor_data = {}

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
        for node in self.graph.node:          
            layer = nn.layer[node.op_type]
            mod = nn.modules

            #for i in layer:
                #if(i < version):
            
           

        #for node in self.graph.node:
        #    input_tensors = [make_tensor_value_info(name, NP_TYPE_TO_TENSOR_TYPE[self.tensor_data[name].dtype], self.tensor_data[name].shape) for name in node.input]
        #    output_tensors = [make_tensor_value_info(name, NP_TYPE_TO_TENSOR_TYPE[self.tensor_data[name].dtype], self.tensor_data[name].shape) for name in node.output]
        #    n_graph = make_graph([node], 'compute_graph', input_tensors, output_tensors)
        #    n_model = make_model(n_graph, producer_name='onnxtester')
        #    n_model.opset_import[0].version = model.opset_import[0].version 
        #    onnx.save(n_model, './model/' + node.name + '.onnx', )

        #self.sessions = dict([(fname.split('.')[0], ort.InferenceSession("./model/" + fname)) for fname in os.listdir('./model')])

        #for node in self.graph.node:
        #    input =  dict([(i_name, self.tensor_data[i_name]) for i_name in node.input])
        #    node.output
        #    out = self.sessions[node.name].run(None, input)
        #    for i,n in enumerate(node.output):
        #        self.tensor_data[n] = out[i]            

        print()