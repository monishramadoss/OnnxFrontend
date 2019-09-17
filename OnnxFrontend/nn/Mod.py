from __future__ import absolute_import
from __future__ import division
import numpy as np

class Mod_10:

	m_fmod = int()
	def __init__(self, _name: str, _tensor: dict, fmod=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_fmod = fmod

	def output(self, C=str()):
		self.m_C = C


	def __call__(self, A=str(), B=str()):
		self.m_A = A
		self.m_B = B

		return (self.tensor[self.m_C])
