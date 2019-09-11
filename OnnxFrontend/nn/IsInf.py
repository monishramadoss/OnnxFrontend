import numpy as np

class IsInf_10:

	detect_negative = m_int()
	detect_positive = m_int()
	def __init__(self, _name: str, detect_negative: int, detect_positive: int):
		self.name = _name
		self.m_detect_negative = detect_negative
		self.m_detect_positive = detect_positive

	def __call__(self, X: str):
		 return Y
