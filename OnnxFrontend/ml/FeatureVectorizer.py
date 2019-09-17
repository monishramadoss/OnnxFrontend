from __future__ import absolute_import
from __future__ import division
import numpy as np

class FeatureVectorizer_1:

	m_inputdimensions = list()
	def __init__(self, _name: str, _tensor: dict, inputdimensions=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_inputdimensions = inputdimensions

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
