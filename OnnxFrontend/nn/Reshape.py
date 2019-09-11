import numpy as np

class Reshape_1:

	consumed_inputs = m_list()
	shape = m_list()
	def __init__(self, _name: str, consumed_inputs: list, shape: list):
		self.name = _name
		self.m_consumed_inputs = consumed_inputs
		self.m_shape = shape

	def __call__(self, data: str):
		 return reshaped


class Reshape_5:

	def __init__(self, _name: str):
		self.name = _name

	def __call__(self, data: str, shape: str):
		 return reshaped
