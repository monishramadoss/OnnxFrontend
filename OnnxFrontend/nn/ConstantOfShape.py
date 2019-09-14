from __future__ import absolute_import
from __future__ import division
import numpy as np

class ConstantOfShape_9:

	m_value = list()
	def __init__(self, _name: str, _tensor: dict, value=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_value = value

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_output])
