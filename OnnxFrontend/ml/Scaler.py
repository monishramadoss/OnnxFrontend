import numpy as np

class Scaler_1:

	offset = m_list()
	scale = m_list()
	def __init__(self, _name: str, offset: list, scale: list):
		self.name = _name
		self.m_offset = offset
		self.m_scale = scale

	def __call__(self, X: str):
		 return Y
