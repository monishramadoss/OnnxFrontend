import numpy as np
from __future__ import absolute_import
from __future__ import division

class LinearClassifier_1:

	classlabels_ints = m_list()
	classlabels_strings = m_list()
	coefficients = m_list()
	intercepts = m_list()
	multi_class = m_int()
	post_transform = m_str()
	def __init__(self, _name: str, _tensor: dict, classlabels_ints: list, classlabels_strings: list, coefficients: list, intercepts: list, multi_class: int, post_transform: str):
		self.name = _name
		self.tensor = _tensor
		self.m_classlabels_ints = classlabels_ints
		self.m_classlabels_strings = classlabels_strings
		self.m_coefficients = coefficients
		self.m_intercepts = intercepts
		self.m_multi_class = multi_class
		self.m_post_transform = post_transform

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y], self.tensor[Z]
