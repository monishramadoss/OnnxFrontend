import numpy as np

class SVMRegressor_1:

	coefficients = m_list()
	kernel_params = m_list()
	kernel_type = m_str()
	n_supports = m_int()
	one_class = m_int()
	post_transform = m_str()
	rho = m_list()
	support_vectors = m_list()
	def __init__(self, _name: str, coefficients: list, kernel_params: list, kernel_type: str, n_supports: int, one_class: int, post_transform: str, rho: list, support_vectors: list):
		self.name = _name
		self.m_coefficients = coefficients
		self.m_kernel_params = kernel_params
		self.m_kernel_type = kernel_type
		self.m_n_supports = n_supports
		self.m_one_class = one_class
		self.m_post_transform = post_transform
		self.m_rho = rho
		self.m_support_vectors = support_vectors

	def __call__(self, X: str):
		 return Y
