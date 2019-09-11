import numpy as np

class Slice_1:

	axes = m_list()
	ends = m_list()
	starts = m_list()
	def __init__(self, _name: str, axes: list, ends: list, starts: list):
		self.name = _name
		self.m_axes = axes
		self.m_ends = ends
		self.m_starts = starts

	def __call__(self, data: str):
		 return output


class Slice_10:

	def __init__(self, _name: str):
		self.name = _name

	def __call__(self, data: str, starts: str, ends: str, axes: str, steps: str):
		 return output
