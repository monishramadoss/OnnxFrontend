import numpy as np
from __future__ import absolute_import
from __future__ import division

class Resize_10:

	mode = m_str()
	def __init__(self, _name: str, _tensor: dict, mode: str):
		self.name = _name
		self.tensor = _tensor
		self.m_mode = mode

	def __call__(self, X: str, scales: str):
		input = (self.tensor[X], self.tensor[scales])
		return self.tensor[Y]
