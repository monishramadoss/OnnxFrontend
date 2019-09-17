from __future__ import absolute_import
from __future__ import division
import numpy as np

class Resize_10:

	m_mode = str()
	def __init__(self, _name: str, _tensor: dict, mode=str()):
		self.name = _name
		self.tensor = _tensor
		self.m_mode = mode

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str(), scales=str()):
		self.m_X = X
		self.m_scales = scales

		return (self.tensor[self.m_Y])
