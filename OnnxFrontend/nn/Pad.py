from __future__ import absolute_import
from __future__ import division
import numpy as np

class Pad_1:

	m_mode = str()
	m_paddings = list()
	m_value = float()
	def __init__(self, _name: str, _tensor: dict, mode=str(), paddings=list(), value=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_mode = mode
		self.m_paddings = paddings
		self.m_value = value

	def output(self, output):
		self.m_output = output


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_output])


class Pad_2:

	m_mode = str()
	m_pads = list()
	m_value = float()
	def __init__(self, _name: str, _tensor: dict, mode=str(), pads=list(), value=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_mode = mode
		self.m_pads = pads
		self.m_value = value

	def output(self, output):
		self.m_output = output


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_output])
