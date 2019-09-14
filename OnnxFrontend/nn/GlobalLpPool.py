from __future__ import absolute_import
from __future__ import division
import numpy as np

class GlobalLpPool_1:

	m_p = float()
	def __init__(self, _name: str, _tensor: dict, p=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_p = p

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])


class GlobalLpPool_2:

	m_p = int()
	def __init__(self, _name: str, _tensor: dict, p=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_p = p

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])
