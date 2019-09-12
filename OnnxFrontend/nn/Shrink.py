import numpy as np
from __future__ import absolute_import
from __future__ import division

class Shrink_9:

	bias = m_float()
	lambd = m_float()
	def __init__(self, _name: str, _tensor: dict, bias: float, lambd: float):
		self.name = _name
		self.tensor = _tensor
		self.m_bias = bias
		self.m_lambd = lambd

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
