import numpy as np
from __future__ import absolute_import
from __future__ import division

class ReduceL1_1:

	axes = m_list()
	keepdims = m_int()
	def __init__(self, _name: str, _tensor: dict, axes: list, keepdims: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axes = axes
		self.m_keepdims = keepdims

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[reduced]
