from __future__ import absolute_import
from __future__ import division
import numpy as np

class GlobalAveragePool_1:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
