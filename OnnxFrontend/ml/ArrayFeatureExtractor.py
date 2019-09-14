from __future__ import absolute_import
from __future__ import division
import numpy as np

class ArrayFeatureExtractor_1:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, Z):
		self.m_Z = Z


	def __call__(self, X: str, Y: str):
		self.m_X = X
		self.m_Y = Y

		return (self.tensor[self.m_Z])
