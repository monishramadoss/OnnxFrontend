from __future__ import absolute_import
from __future__ import division
import numpy as np

class Compress_9:

	m_axis = int()
	def __init__(self, _name: str, _tensor: dict, axis=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str, condition: str):
		self.m_input = input
		self.m_condition = condition

		return (self.tensor[self.m_output])
