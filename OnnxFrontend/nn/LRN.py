import numpy as np

class LRN_1:

	alpha = m_float()
	beta = m_float()
	bias = m_float()
	size = m_int()
	def __init__(self, _name: str, alpha: float, beta: float, bias: float, size: int):
		self.name = _name
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_bias = bias
		self.m_size = size

	def __call__(self, X: str):
		 return Y
