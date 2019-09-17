from __future__ import absolute_import
from __future__ import division
import numpy as np

class MeanVarianceNormalization_9:

	m_axes = list()
	def __init__(self, _name: str, _tensor: dict, axes=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_axes = axes

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
