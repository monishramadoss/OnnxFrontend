import numpy as np

class Clip_1:

	consumed_inputs = m_list()
	max = m_float()
	min = m_float()
	def __init__(self, _name: str, consumed_inputs: list, max: float, min: float):
		self.name = _name
		self.m_consumed_inputs = consumed_inputs
		self.m_max = max
		self.m_min = min

	def __call__(self, input: str):
		 return output


class Clip_6:

	max = m_float()
	min = m_float()
	def __init__(self, _name: str, max: float, min: float):
		self.name = _name
		self.m_max = max
		self.m_min = min

	def __call__(self, input: str):
		 return output
