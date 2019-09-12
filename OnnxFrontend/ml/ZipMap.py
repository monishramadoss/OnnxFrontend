import numpy as np
from __future__ import absolute_import
from __future__ import division

class ZipMap_1:

	classlabels_int64s = m_list()
	classlabels_strings = m_list()
	def __init__(self, _name: str, _tensor: dict, classlabels_int64s: list, classlabels_strings: list):
		self.name = _name
		self.tensor = _tensor
		self.m_classlabels_int64s = classlabels_int64s
		self.m_classlabels_strings = classlabels_strings

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Z]
