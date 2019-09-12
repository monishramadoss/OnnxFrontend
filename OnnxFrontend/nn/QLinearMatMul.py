import numpy as np
from __future__ import absolute_import
from __future__ import division

class QLinearMatMul_10:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, a: str, a_scale: str, a_zero_point: str, b: str, b_scale: str, b_zero_point: str, y_scale: str, y_zero_point: str):
		input = (self.tensor[a], self.tensor[a_scale], self.tensor[a_zero_point], self.tensor[b], self.tensor[b_scale], self.tensor[b_zero_point], self.tensor[y_scale], self.tensor[y_zero_point])
		return self.tensor[y]
