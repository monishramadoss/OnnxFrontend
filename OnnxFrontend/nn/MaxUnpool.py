from __future__ import absolute_import
from __future__ import division
import numpy as np

class MaxUnpool_9:

	m_kernel_shape = list()
	m_pads = list()
	m_strides = list()
	def __init__(self, _name: str, _tensor: dict, kernel_shape=list(), pads=list(), strides=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_strides = strides

	def output(self, output):
		self.m_output = output


	def __call__(self, X: str, I: str, output_shape: str):
		self.m_X = X
		self.m_I = I
		self.m_output_shape = output_shape

		return (self.tensor[self.m_output])
