import numpy as np
from __future__ import absolute_import
from __future__ import division

class LRN_1:

	alpha = m_float()
	beta = m_float()
	bias = m_float()
	size = m_int()
	def __init__(self, _name: str, _tensor: dict, alpha: float, beta: float, bias: float, size: int):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_bias = bias
		self.m_size = size

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
