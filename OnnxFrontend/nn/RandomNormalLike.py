from __future__ import absolute_import
from __future__ import division
import numpy as np

class RandomNormalLike_1:

	m_dtype = int()
	m_mean = float()
	m_scale = float()
	m_seed = float()
	def __init__(self, _name: str, _tensor: dict, dtype=int(), mean=float(), scale=float(), seed=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_dtype = dtype
		self.m_mean = mean
		self.m_scale = scale
		self.m_seed = seed

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_output])
