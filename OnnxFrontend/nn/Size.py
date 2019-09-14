from __future__ import absolute_import
from __future__ import division
import numpy as np

class Size_1:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, size):
		self.m_size = size


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_size])
