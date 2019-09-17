from __future__ import absolute_import
from __future__ import division
import numpy as np

class QuantizeLinear_10:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, y=str()):
		self.m_y = y


	def __call__(self, x=str(), y_scale=str(), y_zero_point=str()):
		self.m_x = x
		self.m_y_scale = y_scale
		self.m_y_zero_point = y_zero_point

		return (self.tensor[self.m_y])
