import numpy as np

class ReverseSequence_10:

	batch_axis = m_int()
	time_axis = m_int()
	def __init__(self, _name: str, batch_axis: int, time_axis: int):
		self.name = _name
		self.m_batch_axis = batch_axis
		self.m_time_axis = time_axis

	def __call__(self, input: str, sequence_lens: str):
		 return Y
