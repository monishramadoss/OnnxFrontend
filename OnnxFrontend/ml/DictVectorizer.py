import numpy as np

class DictVectorizer_1:

	int64_vocabulary = m_list()
	string_vocabulary = m_list()
	def __init__(self, _name: str, int64_vocabulary: list, string_vocabulary: list):
		self.name = _name
		self.m_int64_vocabulary = int64_vocabulary
		self.m_string_vocabulary = string_vocabulary

	def __call__(self, X: str):
		 return Y
