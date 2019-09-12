import numpy as np
from __future__ import absolute_import
from __future__ import division

class ReverseSequence_10:

	batch_axis = m_int()
	time_axis = m_int()
	def __init__(self, _name: str, _tensor: dict, batch_axis: int, time_axis: int):
		self.name = _name
		self.tensor = _tensor
		self.m_batch_axis = batch_axis
		self.m_time_axis = time_axis

	def __call__(self, input: str, sequence_lens: str):
		input = (self.tensor[input], self.tensor[sequence_lens])
		return self.tensor[Y]
