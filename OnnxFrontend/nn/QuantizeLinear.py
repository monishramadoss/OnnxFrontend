import numpy as np
from __future__ import absolute_import
from __future__ import division

class QuantizeLinear_10:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, x: str, y_scale: str, y_zero_point: str):
		input = (self.tensor[x], self.tensor[y_scale], self.tensor[y_zero_point])
		return self.tensor[y]
