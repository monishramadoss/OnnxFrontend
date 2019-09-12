import numpy as np
from __future__ import absolute_import
from __future__ import division

class RandomNormalLike_1:

	dtype = m_int()
	mean = m_float()
	scale = m_float()
	seed = m_float()
	def __init__(self, _name: str, _tensor: dict, dtype: int, mean: float, scale: float, seed: float):
		self.name = _name
		self.tensor = _tensor
		self.m_dtype = dtype
		self.m_mean = mean
		self.m_scale = scale
		self.m_seed = seed

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
