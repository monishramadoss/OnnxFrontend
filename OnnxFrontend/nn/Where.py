from __future__ import absolute_import
from __future__ import division
import numpy as np

class Where_9:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, condition=str(), X=str(), Y=str()):
		self.m_condition = condition
		self.m_X = X
		self.m_Y = Y

		return (self.tensor[self.m_output])
