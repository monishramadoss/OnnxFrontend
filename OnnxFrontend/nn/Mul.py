import numpy as np

class Mul_1:

	axis = m_int()
	broadcast = m_int()
	consumed_inputs = m_list()
	def __init__(self, _name: str, axis: int, broadcast: int, consumed_inputs: list):
		self.name = _name
		self.m_axis = axis
		self.m_broadcast = broadcast
		self.m_consumed_inputs = consumed_inputs

	def __call__(self, A: str, B: str):
		 return C


class Mul_6:

	axis = m_int()
	broadcast = m_int()
	def __init__(self, _name: str, axis: int, broadcast: int):
		self.name = _name
		self.m_axis = axis
		self.m_broadcast = broadcast

	def __call__(self, A: str, B: str):
		 return C


class Mul_7:

	def __init__(self, _name: str):
		self.name = _name

	def __call__(self, A: str, B: str):
		 return C
