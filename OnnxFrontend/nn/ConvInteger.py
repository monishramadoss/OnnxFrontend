import numpy as np

class ConvInteger_10:

	auto_pad = m_str()
	dilations = m_list()
	group = m_int()
	kernel_shape = m_list()
	pads = m_list()
	strides = m_list()
	def __init__(self, _name: str, auto_pad: str, dilations: list, group: int, kernel_shape: list, pads: list, strides: list):
		self.name = _name
		self.m_auto_pad = auto_pad
		self.m_dilations = dilations
		self.m_group = group
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_strides = strides

	def __call__(self, x: str, w: str, x_zero_point: str, w_zero_point: str):
		 return y
