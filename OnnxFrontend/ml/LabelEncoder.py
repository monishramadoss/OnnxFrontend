from __future__ import absolute_import
from __future__ import division
import numpy as np

class LabelEncoder_1:

	m_classes_strings = list()
	m_default_int64 = int()
	m_default_string = str()
	def __init__(self, _name: str, _tensor: dict, classes_strings=list(), default_int64=int(), default_string=str()):
		self.name = _name
		self.tensor = _tensor
		self.m_classes_strings = classes_strings
		self.m_default_int64 = default_int64
		self.m_default_string = default_string

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])


class LabelEncoder_2:

	m_default_float = float()
	m_default_int64 = int()
	m_default_string = str()
	m_keys_floats = list()
	m_keys_int64s = list()
	m_keys_strings = list()
	m_values_floats = list()
	m_values_int64s = list()
	m_values_strings = list()
	def __init__(self, _name: str, _tensor: dict, default_float=float(), default_int64=int(), default_string=str(), keys_floats=list(), keys_int64s=list(), keys_strings=list(), values_floats=list(), values_int64s=list(), values_strings=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_default_float = default_float
		self.m_default_int64 = default_int64
		self.m_default_string = default_string
		self.m_keys_floats = keys_floats
		self.m_keys_int64s = keys_int64s
		self.m_keys_strings = keys_strings
		self.m_values_floats = values_floats
		self.m_values_int64s = values_int64s
		self.m_values_strings = values_strings

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
