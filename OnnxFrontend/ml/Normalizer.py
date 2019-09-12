import numpy as np
from __future__ import absolute_import
from __future__ import division

class Normalizer_1:

	norm = m_str()
	def __init__(self, _name: str, _tensor: dict, norm: str):
		self.name = _name
		self.tensor = _tensor
		self.m_norm = norm

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
