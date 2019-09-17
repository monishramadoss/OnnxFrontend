from __future__ import absolute_import
from __future__ import division
import numpy as np

class Tile_1:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, input=str(), tiles=str(), axis=str()):
		self.m_input = input
		self.m_tiles = tiles
		self.m_axis = axis

		return (self.tensor[self.m_output])


class Tile_6:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, input=str(), repeats=str()):
		self.m_input = input
		self.m_repeats = repeats

		return (self.tensor[self.m_output])
