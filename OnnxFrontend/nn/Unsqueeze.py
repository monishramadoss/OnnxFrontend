from __future__ import absolute_import
from __future__ import division
import numpy as np

class Unsqueeze_1:

	m_axes = list()
	def __init__(self, _name: str, _tensor: dict, axes=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_axes = axes

	def output(self, expanded):
		self.m_expanded = expanded


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_expanded])
