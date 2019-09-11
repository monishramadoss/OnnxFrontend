import numpy as np

class InstanceNormalization_1:

	consumed_inputs = m_list()
	epsilon = m_float()
	def __init__(self, _name: str, consumed_inputs: list, epsilon: float):
		self.name = _name
		self.m_consumed_inputs = consumed_inputs
		self.m_epsilon = epsilon

	def __call__(self, input: str, scale: str, B: str):
		 return output


class InstanceNormalization_6:

	epsilon = m_float()
	def __init__(self, _name: str, epsilon: float):
		self.name = _name
		self.m_epsilon = epsilon

	def __call__(self, input: str, scale: str, B: str):
		 return output
