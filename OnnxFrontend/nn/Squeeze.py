import numpy as np
from __future__ import absolute_import
from __future__ import division

class Squeeze_1:

	axes = m_list()
	def __init__(self, _name: str, _tensor: dict, axes: list):
		self.name = _name
		self.tensor = _tensor
		self.m_axes = axes

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[squeezed]
