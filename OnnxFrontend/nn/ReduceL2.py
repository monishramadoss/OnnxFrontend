from __future__ import absolute_import
from __future__ import division
import numpy as np

class ReduceL2_1:

	m_axes = list()
	m_keepdims = int()
	def __init__(self, _name: str, _tensor: dict, axes=list(), keepdims=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axes = axes
		self.m_keepdims = keepdims

	def output(self, reduced):
		self.m_reduced = reduced


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_reduced])
