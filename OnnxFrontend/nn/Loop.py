from __future__ import absolute_import
from __future__ import division
import numpy as np

class Loop_1:

	m_body = list()
	def __init__(self, _name: str, _tensor: dict, body=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_body = body

	def output(self, v_final_and_scan_outputs):
		self.m_v_final_and_scan_outputs = v_final_and_scan_outputs


	def __call__(self, M: str, cond: str, v_initial: str):
		self.m_M = M
		self.m_cond = cond
		self.m_v_initial = v_initial

		return (self.tensor[self.m_v_final_and_scan_outputs])
