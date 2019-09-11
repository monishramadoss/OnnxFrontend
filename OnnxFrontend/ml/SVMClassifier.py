import numpy as np

class SVMClassifier_1:

	classlabels_ints = m_list()
	classlabels_strings = m_list()
	coefficients = m_list()
	kernel_params = m_list()
	kernel_type = m_str()
	post_transform = m_str()
	prob_a = m_list()
	prob_b = m_list()
	rho = m_list()
	support_vectors = m_list()
	vectors_per_class = m_list()
	def __init__(self, _name: str, classlabels_ints: list, classlabels_strings: list, coefficients: list, kernel_params: list, kernel_type: str, post_transform: str, prob_a: list, prob_b: list, rho: list, support_vectors: list, vectors_per_class: list):
		self.name = _name
		self.m_classlabels_ints = classlabels_ints
		self.m_classlabels_strings = classlabels_strings
		self.m_coefficients = coefficients
		self.m_kernel_params = kernel_params
		self.m_kernel_type = kernel_type
		self.m_post_transform = post_transform
		self.m_prob_a = prob_a
		self.m_prob_b = prob_b
		self.m_rho = rho
		self.m_support_vectors = support_vectors
		self.m_vectors_per_class = vectors_per_class

	def __call__(self, X: str):
		 return Y, Z
