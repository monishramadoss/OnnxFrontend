from __future__ import absolute_import
from __future__ import division
import numpy as np

class Upsample_1:

	m_height_scale = float()
	m_mode = str()
	m_width_scale = float()
	def __init__(self, _name: str, _tensor: dict, height_scale=float(), mode=str(), width_scale=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_height_scale = height_scale
		self.m_mode = mode
		self.m_width_scale = width_scale

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])
