import numpy as np
from __future__ import absolute_import
from __future__ import division

class Multinomial_7:

	dtype = m_int()
	sample_size = m_int()
	seed = m_float()
	def __init__(self, _name: str, _tensor: dict, dtype: int, sample_size: int, seed: float):
		self.name = _name
		self.tensor = _tensor
		self.m_dtype = dtype
		self.m_sample_size = sample_size
		self.m_seed = seed

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
