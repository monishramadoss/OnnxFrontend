from __future__ import absolute_import
from __future__ import division
import numpy as np

class LpNormalization_1:

	m_axis = int()
	m_p = int()
	def __init__(self, _name: str, _tensor: dict, axis=int(), p=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_p = p

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_output])
