from __future__ import absolute_import
from __future__ import division
import numpy as np

class RandomUniformLike_1:

	m_dtype = int()
	m_high = float()
	m_low = float()
	m_seed = float()
	def __init__(self, _name: str, _tensor: dict, dtype=int(), high=float(), low=float(), seed=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_dtype = dtype
		self.m_high = high
		self.m_low = low
		self.m_seed = seed

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, input=str()):
		self.m_input = input

		return (self.tensor[self.m_output])
