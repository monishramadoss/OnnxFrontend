from __future__ import absolute_import
from __future__ import division
import numpy as np

class Squeeze_1:

	m_axes = list()
	def __init__(self, _name: str, _tensor: dict, axes=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_axes = axes

	def output(self, squeezed=str()):
		self.m_squeezed = squeezed


	def __call__(self, data=str()):
		self.m_data = data

		return (self.tensor[self.m_squeezed])
