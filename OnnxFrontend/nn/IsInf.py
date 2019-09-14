from __future__ import absolute_import
from __future__ import division
import numpy as np

class IsInf_10:

	m_detect_negative = int()
	m_detect_positive = int()
	def __init__(self, _name: str, _tensor: dict, detect_negative=int(), detect_positive=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_detect_negative = detect_negative
		self.m_detect_positive = detect_positive

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])
