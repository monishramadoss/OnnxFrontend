from __future__ import absolute_import
from __future__ import division
import numpy as np

class Clip_1:

	m_consumed_inputs = list()
	m_max = float()
	m_min = float()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs=list(), max=float(), min=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_max = max
		self.m_min = min

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_output])


class Clip_6:

	m_max = float()
	m_min = float()
	def __init__(self, _name: str, _tensor: dict, max=float(), min=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_max = max
		self.m_min = min

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_output])
