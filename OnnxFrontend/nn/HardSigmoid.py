from __future__ import absolute_import
from __future__ import division
import numpy as np

class HardSigmoid_1:

	m_alpha = float()
	m_beta = float()
	m_consumed_inputs = list()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), beta=float(), consumed_inputs=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_consumed_inputs = consumed_inputs

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])


class HardSigmoid_6:

	m_alpha = float()
	m_beta = float()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), beta=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_beta = beta

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])
