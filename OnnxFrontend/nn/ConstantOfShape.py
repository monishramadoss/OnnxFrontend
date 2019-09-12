import numpy as np
from __future__ import absolute_import
from __future__ import division

class ConstantOfShape_9:

	value = m_list()
	def __init__(self, _name: str, _tensor: dict, value: list):
		self.name = _name
		self.tensor = _tensor
		self.m_value = value

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
