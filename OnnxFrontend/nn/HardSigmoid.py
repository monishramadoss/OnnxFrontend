import numpy as np

class HardSigmoid_1:

	alpha = m_float()
	beta = m_float()
	consumed_inputs = m_list()
	def __init__(self, _name: str, alpha: float, beta: float, consumed_inputs: list):
		self.name = _name
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_consumed_inputs = consumed_inputs

	def __call__(self, X: str):
		 return Y


class HardSigmoid_6:

	alpha = m_float()
	beta = m_float()
	def __init__(self, _name: str, alpha: float, beta: float):
		self.name = _name
		self.m_alpha = alpha
		self.m_beta = beta

	def __call__(self, X: str):
		 return Y
