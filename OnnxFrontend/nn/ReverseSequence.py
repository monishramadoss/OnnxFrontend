from __future__ import absolute_import
from __future__ import division
import numpy as np

class ReverseSequence_10:

	m_batch_axis = int()
	m_time_axis = int()
	def __init__(self, _name: str, _tensor: dict, batch_axis=int(), time_axis=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_batch_axis = batch_axis
		self.m_time_axis = time_axis

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, input: str, sequence_lens: str):
		self.m_input = input
		self.m_sequence_lens = sequence_lens

		return (self.tensor[self.m_Y])
