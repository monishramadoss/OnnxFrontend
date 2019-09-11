import numpy as np

class LeakyRelu_1:

	alpha = m_float()
	consumed_inputs = m_list()
	def __init__(self, _name: str, alpha: float, consumed_inputs: list):
		self.name = _name
		self.m_alpha = alpha
		self.m_consumed_inputs = consumed_inputs

	def __call__(self, X: str):
		 return Y


class LeakyRelu_6:

	alpha = m_float()
	def __init__(self, _name: str, alpha: float):
		self.name = _name
		self.m_alpha = alpha

	def __call__(self, X: str):
		 return Y
