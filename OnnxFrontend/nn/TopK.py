from __future__ import absolute_import
from __future__ import division
import numpy as np

class TopK_1:

	m_axis = int()
	m_k = int()
	def __init__(self, _name: str, _tensor: dict, axis=int(), k=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_k = k

	def output(self, Values, Indices):
		self.m_Values = Values
		self.m_Indices = Indices


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Values, self.m_Indices])


class TopK_10:

	m_axis = int()
	def __init__(self, _name: str, _tensor: dict, axis=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def output(self, Values, Indices):
		self.m_Values = Values
		self.m_Indices = Indices


	def __call__(self, X: str, K: str):
		self.m_X = X
		self.m_K = K

		return (self.tensor[self.m_Values, self.m_Indices])
