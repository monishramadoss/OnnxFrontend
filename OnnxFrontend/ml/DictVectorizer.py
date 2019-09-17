from __future__ import absolute_import
from __future__ import division
import numpy as np

class DictVectorizer_1:

	m_int64_vocabulary = list()
	m_string_vocabulary = list()
	def __init__(self, _name: str, _tensor: dict, int64_vocabulary=list(), string_vocabulary=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_int64_vocabulary = int64_vocabulary
		self.m_string_vocabulary = string_vocabulary

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
