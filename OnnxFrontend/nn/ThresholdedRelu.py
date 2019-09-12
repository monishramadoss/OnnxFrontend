import numpy as np
from __future__ import absolute_import
from __future__ import division

class ThresholdedRelu_10:

	alpha = m_float()
	def __init__(self, _name: str, _tensor: dict, alpha: float):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
