from __future__ import absolute_import
from __future__ import division
import numpy as np

class RandomUniform_1:

	m_dtype = int()
	m_high = float()
	m_low = float()
	m_seed = float()
	m_shape = list()
	def __init__(self, _name: str, _tensor: dict, dtype=int(), high=float(), low=float(), seed=float(), shape=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_dtype = dtype
		self.m_high = high
		self.m_low = low
		self.m_seed = seed
		self.m_shape = shape

	def output(self, output):
		self.m_output = output


	def __call__(self):
		

		return (self.tensor[self.m_output])
