from __future__ import absolute_import
from __future__ import division
import numpy as np

class Slice_1:

	m_axes = list()
	m_ends = list()
	m_starts = list()
	def __init__(self, _name: str, _tensor: dict, axes=list(), ends=list(), starts=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_axes = axes
		self.m_ends = ends
		self.m_starts = starts

	def output(self, output):
		self.m_output = output


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_output])


class Slice_10:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, output):
		self.m_output = output


	def __call__(self, data: str, starts: str, ends: str, axes: str, steps: str):
		self.m_data = data
		self.m_starts = starts
		self.m_ends = ends
		self.m_axes = axes
		self.m_steps = steps

		return (self.tensor[self.m_output])
