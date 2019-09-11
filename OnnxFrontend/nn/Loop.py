import numpy as np

class Loop_1:

	body = m_list()
	def __init__(self, _name: str, body: list):
		self.name = _name
		self.m_body = body

	def __call__(self, M: str, cond: str, v_initial: str):
		 return v_final_and_scan_outputs
