from __future__ import absolute_import
from __future__ import division
import numpy as np

class ArgMax_1:

	m_axis = int()
	m_keepdims = int()
	def __init__(self, _name: str, _tensor: dict, axis=int(), keepdims=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_keepdims = keepdims

	def output(self, reduced=str()):
		self.m_reduced = reduced


	def __call__(self, data=str()):
		self.m_data = data

		return (self.tensor[self.m_reduced])
