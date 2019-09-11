import numpy as np

class LinearClassifier_1:

	classlabels_ints = m_list()
	classlabels_strings = m_list()
	coefficients = m_list()
	intercepts = m_list()
	multi_class = m_int()
	post_transform = m_str()
	def __init__(self, _name: str, classlabels_ints: list, classlabels_strings: list, coefficients: list, intercepts: list, multi_class: int, post_transform: str):
		self.name = _name
		self.m_classlabels_ints = classlabels_ints
		self.m_classlabels_strings = classlabels_strings
		self.m_coefficients = coefficients
		self.m_intercepts = intercepts
		self.m_multi_class = multi_class
		self.m_post_transform = post_transform

	def __call__(self, X: str):
		 return Y, Z
