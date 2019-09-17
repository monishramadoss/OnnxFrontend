from __future__ import absolute_import
from __future__ import division
import numpy as np

class MatMul_1:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, A=str(), B=str()):
		self.m_A = A
		self.m_B = B

		return (self.tensor[self.m_Y])


class MatMul_9:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, A=str(), B=str()):
		self.m_A = A
		self.m_B = B

		return (self.tensor[self.m_Y])
