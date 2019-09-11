import numpy as np

class RandomUniformLike_1:

	dtype = m_int()
	high = m_float()
	low = m_float()
	seed = m_float()
	def __init__(self, _name: str, dtype: int, high: float, low: float, seed: float):
		self.name = _name
		self.m_dtype = dtype
		self.m_high = high
		self.m_low = low
		self.m_seed = seed

	def __call__(self, input: str):
		 return output
