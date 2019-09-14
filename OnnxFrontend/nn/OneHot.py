from __future__ import absolute_import
from __future__ import division
import numpy as np

class OneHot_9:

	m_axis = int()
	def __init__(self, _name: str, _tensor: dict, axis=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def output(self, output):
		self.m_output = output


	def __call__(self, indices: str, depth: str, values: str):
		self.m_indices = indices
		self.m_depth = depth
		self.m_values = values

		return (self.tensor[self.m_output])
