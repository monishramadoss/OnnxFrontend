from __future__ import absolute_import
from __future__ import division
import numpy as np

class StringNormalizer_10:

	m_case_change_action = str()
	m_is_case_sensitive = int()
	m_locale = str()
	m_stopwords = list()
	def __init__(self, _name: str, _tensor: dict, case_change_action=str(), is_case_sensitive=int(), locale=str(), stopwords=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_case_change_action = case_change_action
		self.m_is_case_sensitive = is_case_sensitive
		self.m_locale = locale
		self.m_stopwords = stopwords

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
