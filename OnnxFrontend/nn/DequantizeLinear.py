from __future__ import absolute_import
from __future__ import division
import numpy as np

class DequantizeLinear_10:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, y):
		self.m_y = y


	def __call__(self, x: str, x_scale: str, x_zero_point: str):
		self.m_x = x
		self.m_x_scale = x_scale
		self.m_x_zero_point = x_zero_point

		return (self.tensor[self.m_y])
