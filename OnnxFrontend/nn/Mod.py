import numpy as np
from __future__ import absolute_import
from __future__ import division

class Mod_10:

	fmod = m_int()
	def __init__(self, _name: str, _tensor: dict, fmod: int):
		self.name = _name
		self.tensor = _tensor
		self.m_fmod = fmod

	def __call__(self, A: str, B: str):
		input = (self.tensor[A], self.tensor[B])
		return self.tensor[C]
