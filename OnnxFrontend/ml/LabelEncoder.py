import numpy as np

class LabelEncoder_1:

	classes_strings = m_list()
	default_int64 = m_int()
	default_string = m_str()
	def __init__(self, _name: str, classes_strings: list, default_int64: int, default_string: str):
		self.name = _name
		self.m_classes_strings = classes_strings
		self.m_default_int64 = default_int64
		self.m_default_string = default_string

	def __call__(self, X: str):
		 return Y


class LabelEncoder_2:

	default_float = m_float()
	default_int64 = m_int()
	default_string = m_str()
	keys_floats = m_list()
	keys_int64s = m_list()
	keys_strings = m_list()
	values_floats = m_list()
	values_int64s = m_list()
	values_strings = m_list()
	def __init__(self, _name: str, default_float: float, default_int64: int, default_string: str, keys_floats: list, keys_int64s: list, keys_strings: list, values_floats: list, values_int64s: list, values_strings: list):
		self.name = _name
		self.m_default_float = default_float
		self.m_default_int64 = default_int64
		self.m_default_string = default_string
		self.m_keys_floats = keys_floats
		self.m_keys_int64s = keys_int64s
		self.m_keys_strings = keys_strings
		self.m_values_floats = values_floats
		self.m_values_int64s = values_int64s
		self.m_values_strings = values_strings

	def __call__(self, X: str):
		 return Y
