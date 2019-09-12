import numpy as np
from __future__ import absolute_import
from __future__ import division

class MatMulInteger_10:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, A: str, B: str, a_zero_point: str, b_zero_point: str):
		input = (self.tensor[A], self.tensor[B], self.tensor[a_zero_point], self.tensor[b_zero_point])
		return self.tensor[Y]
