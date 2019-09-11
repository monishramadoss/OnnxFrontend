import numpy as np

class MaxUnpool_9:

	kernel_shape = m_list()
	pads = m_list()
	strides = m_list()
	def __init__(self, _name: str, kernel_shape: list, pads: list, strides: list):
		self.name = _name
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_strides = strides

	def __call__(self, X: str, I: str, output_shape: str):
		 return output
