import numpy as np
from __future__ import absolute_import
from __future__ import division

class Binarizer_1:

	threshold = m_float()
	def __init__(self, _name: str, _tensor: dict, threshold: float):
		self.name = _name
		self.tensor = _tensor
		self.m_threshold = threshold

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
