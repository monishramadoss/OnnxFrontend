from __future__ import absolute_import
from __future__ import division
import numpy as np

class Gather_1:

	m_axis = int()
	def __init__(self, _name: str, _tensor: dict, axis=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, data=str(), indices=str()):
		self.m_data = data
		self.m_indices = indices

		return (self.tensor[self.m_output])
