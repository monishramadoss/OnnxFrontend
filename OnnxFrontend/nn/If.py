from __future__ import absolute_import
from __future__ import division
import numpy as np

class If_1:

	m_else_branch = list()
	m_then_branch = list()
	def __init__(self, _name: str, _tensor: dict, else_branch=list(), then_branch=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_else_branch = else_branch
		self.m_then_branch = then_branch

	def output(self, outputs=str()):
		self.m_outputs = outputs


	def __call__(self, cond=str()):
		self.m_cond = cond

		return (self.tensor[self.m_outputs])
