import numpy as np
from __future__ import absolute_import
from __future__ import division

class Split_1:

	axis = m_int()
	split = m_list()
	def __init__(self, _name: str, _tensor: dict, axis: int, split: list):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_split = split

	def __call__(self, input: str, split: str):
		input = (self.tensor[input], self.tensor[split])
		return self.tensor[outputs...]


class Split_2:

	axis = m_int()
	split = m_list()
	def __init__(self, _name: str, _tensor: dict, axis: int, split: list):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_split = split

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[outputs]
