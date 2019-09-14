from __future__ import absolute_import
from __future__ import division
import numpy as np

class Transpose_1:

	m_perm = list()
	def __init__(self, _name: str, _tensor: dict, perm=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_perm = perm

	def output(self, transposed):
		self.m_transposed = transposed


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_transposed])
