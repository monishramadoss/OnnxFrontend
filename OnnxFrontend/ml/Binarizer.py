from __future__ import absolute_import
from __future__ import division
import numpy as np

class Binarizer_1:

	m_threshold = float()
	def __init__(self, _name: str, _tensor: dict, threshold=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_threshold = threshold

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
