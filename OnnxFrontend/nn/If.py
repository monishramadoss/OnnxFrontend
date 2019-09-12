import numpy as np
from __future__ import absolute_import
from __future__ import division

class If_1:

	else_branch = m_list()
	then_branch = m_list()
	def __init__(self, _name: str, _tensor: dict, else_branch: list, then_branch: list):
		self.name = _name
		self.tensor = _tensor
		self.m_else_branch = else_branch
		self.m_then_branch = then_branch

	def __call__(self, cond: str):
		input = (self.tensor[cond])
		return self.tensor[outputs]
