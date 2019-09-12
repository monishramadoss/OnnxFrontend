import numpy as np
from __future__ import absolute_import
from __future__ import division

class LpPool_1:

	auto_pad = m_str()
	kernel_shape = m_list()
	p = m_float()
	pads = m_list()
	strides = m_list()
	def __init__(self, _name: str, _tensor: dict, auto_pad: str, kernel_shape: list, p: float, pads: list, strides: list):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_kernel_shape = kernel_shape
		self.m_p = p
		self.m_pads = pads
		self.m_strides = strides

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]


class LpPool_2:

	auto_pad = m_str()
	kernel_shape = m_list()
	p = m_int()
	pads = m_list()
	strides = m_list()
	def __init__(self, _name: str, _tensor: dict, auto_pad: str, kernel_shape: list, p: int, pads: list, strides: list):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_kernel_shape = kernel_shape
		self.m_p = p
		self.m_pads = pads
		self.m_strides = strides

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
