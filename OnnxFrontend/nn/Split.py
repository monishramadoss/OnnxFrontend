from __future__ import absolute_import
from __future__ import division
import numpy as np

class Split_1:

	m_axis = int()
	m_split = list()
	def __init__(self, _name: str, _tensor: dict, axis=int(), split=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_split = split

	def output(self, outputs):
		self.m_outputs = outputs


	def __call__(self, input: str, split: str):
		self.m_input = input
		self.m_split = split

		return (self.tensor[self.m_outputs])


class Split_2:

	m_axis = int()
	m_split = list()
	def __init__(self, _name: str, _tensor: dict, axis=int(), split=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_split = split

	def output(self, outputs):
		self.m_outputs = outputs


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_outputs])
