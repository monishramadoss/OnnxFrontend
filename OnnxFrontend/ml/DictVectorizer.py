import numpy as np
from __future__ import absolute_import
from __future__ import division

class DictVectorizer_1:

	int64_vocabulary = m_list()
	string_vocabulary = m_list()
	def __init__(self, _name: str, _tensor: dict, int64_vocabulary: list, string_vocabulary: list):
		self.name = _name
		self.tensor = _tensor
		self.m_int64_vocabulary = int64_vocabulary
		self.m_string_vocabulary = string_vocabulary

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
