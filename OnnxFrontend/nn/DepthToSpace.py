from __future__ import absolute_import
from __future__ import division
import numpy as np

class DepthToSpace_1:

	m_blocksize = int()
	def __init__(self, _name: str, _tensor: dict, blocksize=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_blocksize = blocksize

	def output(self, output):
		self.m_output = output


	def __call__(self, input: str):
		self.m_input = input

		return (self.tensor[self.m_output])
