import numpy as np

class If_1:

	else_branch = m_list()
	then_branch = m_list()
	def __init__(self, _name: str, else_branch: list, then_branch: list):
		self.name = _name
		self.m_else_branch = else_branch
		self.m_then_branch = then_branch

	def __call__(self, cond: str):
		 return outputs
