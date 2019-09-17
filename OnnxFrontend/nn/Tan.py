from __future__ import absolute_import
from __future__ import division
import numpy as np

class Tan_7:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, input=str()):
		self.m_input = input

		return (self.tensor[self.m_output])
