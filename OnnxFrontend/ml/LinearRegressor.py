from __future__ import absolute_import
from __future__ import division
import numpy as np

class LinearRegressor_1:

	m_coefficients = list()
	m_intercepts = list()
	m_post_transform = str()
	m_targets = int()
	def __init__(self, _name: str, _tensor: dict, coefficients=list(), intercepts=list(), post_transform=str(), targets=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_coefficients = coefficients
		self.m_intercepts = intercepts
		self.m_post_transform = post_transform
		self.m_targets = targets

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
