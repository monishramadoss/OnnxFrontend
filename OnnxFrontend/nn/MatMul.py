import numpy as np
from __future__ import absolute_import
from __future__ import division

class MatMul_1:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, A: str, B: str):
		input = (self.tensor[A], self.tensor[B])
		return self.tensor[Y]


class MatMul_9:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, A: str, B: str):
		input = (self.tensor[A], self.tensor[B])
		return self.tensor[Y]
