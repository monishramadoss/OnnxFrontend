import numpy as np
from __future__ import absolute_import
from __future__ import division

class Transpose_1:

	perm = m_list()
	def __init__(self, _name: str, _tensor: dict, perm: list):
		self.name = _name
		self.tensor = _tensor
		self.m_perm = perm

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[transposed]
