import numpy as np
from __future__ import absolute_import
from __future__ import division

class FeatureVectorizer_1:

	inputdimensions = m_list()
	def __init__(self, _name: str, _tensor: dict, inputdimensions: list):
		self.name = _name
		self.tensor = _tensor
		self.m_inputdimensions = inputdimensions

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
