import numpy as np
from __future__ import absolute_import
from __future__ import division

class Slice_1:

	axes = m_list()
	ends = m_list()
	starts = m_list()
	def __init__(self, _name: str, _tensor: dict, axes: list, ends: list, starts: list):
		self.name = _name
		self.tensor = _tensor
		self.m_axes = axes
		self.m_ends = ends
		self.m_starts = starts

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[output]


class Slice_10:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, data: str, starts: str, ends: str, axes: str, steps: str):
		input = (self.tensor[data], self.tensor[starts], self.tensor[ends], self.tensor[axes], self.tensor[steps])
		return self.tensor[output]
