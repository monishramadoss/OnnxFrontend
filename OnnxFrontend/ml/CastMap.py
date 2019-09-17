from __future__ import absolute_import
from __future__ import division
import numpy as np

class CastMap_1:

	m_cast_to = str()
	m_map_form = str()
	m_max_map = int()
	def __init__(self, _name: str, _tensor: dict, cast_to=str(), map_form=str(), max_map=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_cast_to = cast_to
		self.m_map_form = map_form
		self.m_max_map = max_map

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
