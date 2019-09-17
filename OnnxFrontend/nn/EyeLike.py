from __future__ import absolute_import
from __future__ import division
import numpy as np

class EyeLike_9:

	m_dtype = int()
	m_k = int()
	def __init__(self, _name: str, _tensor: dict, dtype=int(), k=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_dtype = dtype
		self.m_k = k

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, input=str()):
		self.m_input = input

		return (self.tensor[self.m_output])
