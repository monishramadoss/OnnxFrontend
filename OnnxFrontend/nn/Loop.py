import numpy as np
from __future__ import absolute_import
from __future__ import division

class Loop_1:

	body = m_list()
	def __init__(self, _name: str, _tensor: dict, body: list):
		self.name = _name
		self.tensor = _tensor
		self.m_body = body

	def __call__(self, M: str, cond: str, v_initial: str):
		input = (self.tensor[M], self.tensor[cond], self.tensor[v_initial])
		return self.tensor[v_final_and_scan_outputs]
