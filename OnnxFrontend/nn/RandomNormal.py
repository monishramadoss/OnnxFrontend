import numpy as np
from __future__ import absolute_import
from __future__ import division

class RandomNormal_1:

	dtype = m_int()
	mean = m_float()
	scale = m_float()
	seed = m_float()
	shape = m_list()
	def __init__(self, _name: str, _tensor: dict, dtype: int, mean: float, scale: float, seed: float, shape: list):
		self.name = _name
		self.tensor = _tensor
		self.m_dtype = dtype
		self.m_mean = mean
		self.m_scale = scale
		self.m_seed = seed
		self.m_shape = shape

	def __call__(self):
		input = ()
		return self.tensor[output]
