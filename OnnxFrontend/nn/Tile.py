import numpy as np
from __future__ import absolute_import
from __future__ import division

class Tile_1:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, input: str, tiles: str, axis: str):
		input = (self.tensor[input], self.tensor[tiles], self.tensor[axis])
		return self.tensor[output]


class Tile_6:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, input: str, repeats: str):
		input = (self.tensor[input], self.tensor[repeats])
		return self.tensor[output]
