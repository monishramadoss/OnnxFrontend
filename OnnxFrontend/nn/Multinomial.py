import numpy as np

class Multinomial_7:

	dtype = m_int()
	sample_size = m_int()
	seed = m_float()
	def __init__(self, _name: str, dtype: int, sample_size: int, seed: float):
		self.name = _name
		self.m_dtype = dtype
		self.m_sample_size = sample_size
		self.m_seed = seed

	def __call__(self, input: str):
		 return output
