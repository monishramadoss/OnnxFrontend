import numpy as np
from __future__ import absolute_import
from __future__ import division

class Size_1:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[size]
