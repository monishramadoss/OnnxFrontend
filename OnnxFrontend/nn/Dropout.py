import numpy as np

class Dropout_1:

	consumed_inputs = m_list()
	is_test = m_int()
	ratio = m_float()
	def __init__(self, _name: str, consumed_inputs: list, is_test: int, ratio: float):
		self.name = _name
		self.m_consumed_inputs = consumed_inputs
		self.m_is_test = is_test
		self.m_ratio = ratio

	def __call__(self, data: str):
		 return output, mask


class Dropout_6:

	is_test = m_int()
	ratio = m_float()
	def __init__(self, _name: str, is_test: int, ratio: float):
		self.name = _name
		self.m_is_test = is_test
		self.m_ratio = ratio

	def __call__(self, data: str):
		 return output, mask


class Dropout_7:

	ratio = m_float()
	def __init__(self, _name: str, ratio: float):
		self.name = _name
		self.m_ratio = ratio

	def __call__(self, data: str):
		 return output, mask


class Dropout_10:

	ratio = m_float()
	def __init__(self, _name: str, ratio: float):
		self.name = _name
		self.m_ratio = ratio

	def __call__(self, data: str):
		 return output, mask
