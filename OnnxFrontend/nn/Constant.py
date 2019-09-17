from __future__ import absolute_import
from __future__ import division
import numpy as np

class Constant_1:

	m_value = list()
	def __init__(self, _name: str, _tensor: dict, value=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_value = value

	def output(self, output=str()):
		self.m_output = output


	def __call__(self):
		

		return (self.tensor[self.m_output])


class Constant_9:

	m_value = list()
	def __init__(self, _name: str, _tensor: dict, value=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_value = value

	def output(self, output=str()):
		self.m_output = output


	def __call__(self):
		

		return (self.tensor[self.m_output])
