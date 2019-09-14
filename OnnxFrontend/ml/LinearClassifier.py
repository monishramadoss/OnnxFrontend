from __future__ import absolute_import
from __future__ import division
import numpy as np

class LinearClassifier_1:

	m_classlabels_ints = list()
	m_classlabels_strings = list()
	m_coefficients = list()
	m_intercepts = list()
	m_multi_class = int()
	m_post_transform = str()
	def __init__(self, _name: str, _tensor: dict, classlabels_ints=list(), classlabels_strings=list(), coefficients=list(), intercepts=list(), multi_class=int(), post_transform=str()):
		self.name = _name
		self.tensor = _tensor
		self.m_classlabels_ints = classlabels_ints
		self.m_classlabels_strings = classlabels_strings
		self.m_coefficients = coefficients
		self.m_intercepts = intercepts
		self.m_multi_class = multi_class
		self.m_post_transform = post_transform

	def output(self, Y, Z):
		self.m_Y = Y
		self.m_Z = Z


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y, self.m_Z])
