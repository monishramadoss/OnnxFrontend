from __future__ import absolute_import
from __future__ import division
import numpy as np

class Scatter_9:

	m_axis = int()
	def __init__(self, _name: str, _tensor: dict, axis=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, data=str(), indices=str(), updates=str()):
		self.m_data = data
		self.m_indices = indices
		self.m_updates = updates

		return (self.tensor[self.m_output])
