from __future__ import absolute_import
from __future__ import division
import numpy as np

class Normalizer_1:

	m_norm = str()
	def __init__(self, _name: str, _tensor: dict, norm=str()):
		self.name = _name
		self.tensor = _tensor
		self.m_norm = norm

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])
