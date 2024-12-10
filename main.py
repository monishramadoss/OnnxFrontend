import _onnx
import _onnx.onnx_module_builder as omb

if __name__ == '__main__':
    omb.build('c', './out', True)