from __future__ import absolute_import
from __future__ import division
import numpy as np

class SVMRegressor_1:

	m_coefficients = list()
	m_kernel_params = list()
	m_kernel_type = str()
	m_n_supports = int()
	m_one_class = int()
	m_post_transform = str()
	m_rho = list()
	m_support_vectors = list()
	def __init__(self, _name: str, _tensor: dict, coefficients=list(), kernel_params=list(), kernel_type=str(), n_supports=int(), one_class=int(), post_transform=str(), rho=list(), support_vectors=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_coefficients = coefficients
		self.m_kernel_params = kernel_params
		self.m_kernel_type = kernel_type
		self.m_n_supports = n_supports
		self.m_one_class = one_class
		self.m_post_transform = post_transform
		self.m_rho = rho
		self.m_support_vectors = support_vectors

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
