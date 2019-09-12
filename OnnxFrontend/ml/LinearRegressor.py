import numpy as np
from __future__ import absolute_import
from __future__ import division

class LinearRegressor_1:

	coefficients = m_list()
	intercepts = m_list()
	post_transform = m_str()
	targets = m_int()
	def __init__(self, _name: str, _tensor: dict, coefficients: list, intercepts: list, post_transform: str, targets: int):
		self.name = _name
		self.tensor = _tensor
		self.m_coefficients = coefficients
		self.m_intercepts = intercepts
		self.m_post_transform = post_transform
		self.m_targets = targets

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
