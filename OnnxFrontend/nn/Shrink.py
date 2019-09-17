from __future__ import absolute_import
from __future__ import division
import numpy as np

class Shrink_9:

	m_bias = float()
	m_lambd = float()
	def __init__(self, _name: str, _tensor: dict, bias=float(), lambd=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_bias = bias
		self.m_lambd = lambd

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, input=str()):
		self.m_input = input

		return (self.tensor[self.m_output])
