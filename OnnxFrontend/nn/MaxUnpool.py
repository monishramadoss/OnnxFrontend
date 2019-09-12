import numpy as np
from __future__ import absolute_import
from __future__ import division

class MaxUnpool_9:

	kernel_shape = m_list()
	pads = m_list()
	strides = m_list()
	def __init__(self, _name: str, _tensor: dict, kernel_shape: list, pads: list, strides: list):
		self.name = _name
		self.tensor = _tensor
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_strides = strides

	def __call__(self, X: str, I: str, output_shape: str):
		input = (self.tensor[X], self.tensor[I], self.tensor[output_shape])
		return self.tensor[output]
