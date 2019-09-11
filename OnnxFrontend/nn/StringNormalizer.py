import numpy as np

class StringNormalizer_10:

	case_change_action = m_str()
	is_case_sensitive = m_int()
	locale = m_str()
	stopwords = m_list()
	def __init__(self, _name: str, case_change_action: str, is_case_sensitive: int, locale: str, stopwords: list):
		self.name = _name
		self.m_case_change_action = case_change_action
		self.m_is_case_sensitive = is_case_sensitive
		self.m_locale = locale
		self.m_stopwords = stopwords

	def __call__(self, X: str):
		 return Y
