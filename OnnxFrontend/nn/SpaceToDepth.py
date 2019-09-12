import numpy as np
from __future__ import absolute_import
from __future__ import division

class SpaceToDepth_1:

	blocksize = m_int()
	def __init__(self, _name: str, _tensor: dict, blocksize: int):
		self.name = _name
		self.tensor = _tensor
		self.m_blocksize = blocksize

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
