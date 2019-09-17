from __future__ import absolute_import
from __future__ import division
import numpy as np

class QLinearMatMul_10:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, y=str()):
		self.m_y = y


	def __call__(self, a=str(), a_scale=str(), a_zero_point=str(), b=str(), b_scale=str(), b_zero_point=str(), y_scale=str(), y_zero_point=str()):
		self.m_a = a
		self.m_a_scale = a_scale
		self.m_a_zero_point = a_zero_point
		self.m_b = b
		self.m_b_scale = b_scale
		self.m_b_zero_point = b_zero_point
		self.m_y_scale = y_scale
		self.m_y_zero_point = y_zero_point

		return (self.tensor[self.m_y])
