import numpy as np
from __future__ import absolute_import
from __future__ import division

class Expand_8:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, input: str, shape: str):
		input = (self.tensor[input], self.tensor[shape])
		return self.tensor[output]
