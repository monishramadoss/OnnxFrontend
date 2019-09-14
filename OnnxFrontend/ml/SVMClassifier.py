from __future__ import absolute_import
from __future__ import division
import numpy as np

class SVMClassifier_1:

	m_classlabels_ints = list()
	m_classlabels_strings = list()
	m_coefficients = list()
	m_kernel_params = list()
	m_kernel_type = str()
	m_post_transform = str()
	m_prob_a = list()
	m_prob_b = list()
	m_rho = list()
	m_support_vectors = list()
	m_vectors_per_class = list()
	def __init__(self, _name: str, _tensor: dict, classlabels_ints=list(), classlabels_strings=list(), coefficients=list(), kernel_params=list(), kernel_type=str(), post_transform=str(), prob_a=list(), prob_b=list(), rho=list(), support_vectors=list(), vectors_per_class=list()):
		self.name = _name
		self.tensor = _tensor
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

	def output(self, Y, Z):
		self.m_Y = Y
		self.m_Z = Z


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y, self.m_Z])
