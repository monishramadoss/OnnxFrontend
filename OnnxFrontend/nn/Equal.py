from __future__ import absolute_import
from __future__ import division
import numpy as np

class Equal_1:

	m_axis = int()
	m_broadcast = int()
	def __init__(self, _name: str, _tensor: dict, axis=int(), broadcast=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_broadcast = broadcast

	def output(self, C=str()):
		self.m_C = C


	def __call__(self, A=str(), B=str()):
		self.m_A = A
		self.m_B = B

		return (self.tensor[self.m_C])


class Equal_7:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, C=str()):
		self.m_C = C


	def __call__(self, A=str(), B=str()):
		self.m_A = A
		self.m_B = B

		return (self.tensor[self.m_C])
