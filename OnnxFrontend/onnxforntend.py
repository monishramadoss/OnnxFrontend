import nn 
import ml

from collections import namedtuple
from typing import Text, Sequence, Any, Type, Tuple, NewType, Optional, Dict

import six
import numpy

import onnx.checker
import onnx.onnx_cpp2py_export.checker as c_checker
from onnx import ModelProto, NodeProto, IR_VERSION


class DeviceType(object):
    _Type = NewType('_Type', int)
    CPU = _Type(0)
    CUDA = _Type(1)
    GPU = _Type(2)


class Device(object):
    def __init__(self, device):
        options = device.split(':')
        self.type = getattr(DeviceType, options[0])
        self.device_id = 0
        if len(options) > 1:
            self.device_id = int(options[1])

def namedtupledict(typename, field_names, *args, **kwargs):
    field_names_map = {n: i for i, n in enumerate(field_names)}
    kwargs.setdefault(str('rename'), True)
    data = namedtuple(typename, field_names, *args, **kwargs)

    def getitem(self, key):
        if isinstance(key, six.string_types):
            key = field_names_map[key]
        return super(type(self), self).__getitem__(key)
    data.__getitem__ = getitem
    return data


class BackendRep(object):
    def run(self, inputs, **kwargs):
        pass

class Backend(object):
    @classmethod
    def is_compatible(cls, model, device='CPU', **kwargs):
        return True

    @classmethod
    def prepare(cls, model, device='CPU', **kwargs):
        onnx.checker.check_model(model)
        return None

    @classmethod
    def run_model(cls, model, inputs, device='CPU', **kwargs):
        backend = cls.prepare(model, device, **kwargs)
        assert backend is not None
        return backend.run(inputs)

    @classmethod
    def run_node(cls, node, inputs, device='CPU', outputs_info=None,  **kwargs):
        if 'opset_version' in kwargs:
            special_context = c_checker.CheckerContext()
            special_context.ir_version = IR_VERSION
            special_context.opset_imports = {'': kwargs['opset_version']}
            onnx.checker.check_node(node, special_context)
        else:
            onnx.checker.check_node(node)
        return None

    @classmethod
    def supports_device(cls, device):
        return True