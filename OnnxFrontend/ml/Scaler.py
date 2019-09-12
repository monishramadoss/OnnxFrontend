import numpy as np
from __future__ import absolute_import
from __future__ import division

class Scaler_1:

	offset = m_list()
	scale = m_list()
	def __init__(self, _name: str, _tensor: dict, offset: list, scale: list):
		self.name = _name
		self.tensor = _tensor
		self.m_offset = offset
		self.m_scale = scale

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
