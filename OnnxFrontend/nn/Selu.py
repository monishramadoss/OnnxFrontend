import numpy as np

class Selu_1:

	alpha = m_float()
	consumed_inputs = m_list()
	gamma = m_float()
	def __init__(self, _name: str, alpha: float, consumed_inputs: list, gamma: float):
		self.name = _name
		self.m_alpha = alpha
		self.m_consumed_inputs = consumed_inputs
		self.m_gamma = gamma

	def __call__(self, X: str):
		 return Y


class Selu_6:

	alpha = m_float()
	gamma = m_float()
	def __init__(self, _name: str, alpha: float, gamma: float):
		self.name = _name
		self.m_alpha = alpha
		self.m_gamma = gamma

	def __call__(self, X: str):
		 return Y
