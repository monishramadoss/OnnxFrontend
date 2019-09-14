from __future__ import absolute_import
from __future__ import division
import numpy as np

class Cast_1:

	m_to = str()
	def __init__(self, _name: str, _tensor: dict, to=str()):
		self.name = _name
		self.tensor = _tensor
		self.m_to = to

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_output])


class Cast_6:

	m_to = int()
	def __init__(self, _name: str, _tensor: dict, to=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_to = to

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_output])


class Cast_9:

	m_to = int()
	def __init__(self, _name: str, _tensor: dict, to=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_to = to

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_output])
