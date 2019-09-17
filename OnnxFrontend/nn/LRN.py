from __future__ import absolute_import
from __future__ import division
import numpy as np

class LRN_1:

	m_alpha = float()
	m_beta = float()
	m_bias = float()
	m_size = int()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), beta=float(), bias=float(), size=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_bias = bias
		self.m_size = size

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
