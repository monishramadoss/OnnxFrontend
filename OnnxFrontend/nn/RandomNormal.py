from __future__ import absolute_import
from __future__ import division
import numpy as np

class RandomNormal_1:

	m_dtype = int()
	m_mean = float()
	m_scale = float()
	m_seed = float()
	m_shape = list()
	def __init__(self, _name: str, _tensor: dict, dtype=int(), mean=float(), scale=float(), seed=float(), shape=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_dtype = dtype
		self.m_mean = mean
		self.m_scale = scale
		self.m_seed = seed
		self.m_shape = shape

	def output(self, output=str()):
		self.m_output = output


	def __call__(self):
		

		return (self.tensor[self.m_output])
