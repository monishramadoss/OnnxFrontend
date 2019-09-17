from __future__ import absolute_import
from __future__ import division
import numpy as np

class ZipMap_1:

	m_classlabels_int64s = list()
	m_classlabels_strings = list()
	def __init__(self, _name: str, _tensor: dict, classlabels_int64s=list(), classlabels_strings=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_classlabels_int64s = classlabels_int64s
		self.m_classlabels_strings = classlabels_strings

	def output(self, Z=str()):
		self.m_Z = Z


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Z])
