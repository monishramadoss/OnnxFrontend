import numpy as np
from __future__ import absolute_import
from __future__ import division

class IsInf_10:

	detect_negative = m_int()
	detect_positive = m_int()
	def __init__(self, _name: str, _tensor: dict, detect_negative: int, detect_positive: int):
		self.name = _name
		self.tensor = _tensor
		self.m_detect_negative = detect_negative
		self.m_detect_positive = detect_positive

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
