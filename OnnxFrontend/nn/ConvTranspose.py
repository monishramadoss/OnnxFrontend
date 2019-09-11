import numpy as np

class ConvTranspose_1:

	auto_pad = m_str()
	dilations = m_list()
	group = m_int()
	kernel_shape = m_list()
	output_padding = m_list()
	output_shape = m_list()
	pads = m_list()
	strides = m_list()
	def __init__(self, _name: str, auto_pad: str, dilations: list, group: int, kernel_shape: list, output_padding: list, output_shape: list, pads: list, strides: list):
		self.name = _name
		self.m_auto_pad = auto_pad
		self.m_dilations = dilations
		self.m_group = group
		self.m_kernel_shape = kernel_shape
		self.m_output_padding = output_padding
		self.m_output_shape = output_shape
		self.m_pads = pads
		self.m_strides = strides

	def __call__(self, X: str, W: str, B: str):
		 return Y
