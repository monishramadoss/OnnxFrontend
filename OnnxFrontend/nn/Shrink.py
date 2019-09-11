import numpy as np

class Shrink_9:

	bias = m_float()
	lambd = m_float()
	def __init__(self, _name: str, bias: float, lambd: float):
		self.name = _name
		self.m_bias = bias
		self.m_lambd = lambd

	def __call__(self, input: str):
		 return output
