import numpy as np

class LpPool_1:

	auto_pad = m_str()
	kernel_shape = m_list()
	p = m_float()
	pads = m_list()
	strides = m_list()
	def __init__(self, _name: str, auto_pad: str, kernel_shape: list, p: float, pads: list, strides: list):
		self.name = _name
		self.m_auto_pad = auto_pad
		self.m_kernel_shape = kernel_shape
		self.m_p = p
		self.m_pads = pads
		self.m_strides = strides

	def __call__(self, X: str):
		 return Y


class LpPool_2:

	auto_pad = m_str()
	kernel_shape = m_list()
	p = m_int()
	pads = m_list()
	strides = m_list()
	def __init__(self, _name: str, auto_pad: str, kernel_shape: list, p: int, pads: list, strides: list):
		self.name = _name
		self.m_auto_pad = auto_pad
		self.m_kernel_shape = kernel_shape
		self.m_p = p
		self.m_pads = pads
		self.m_strides = strides

	def __call__(self, X: str):
		 return Y
