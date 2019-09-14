from __future__ import absolute_import
from __future__ import division
import numpy as np

class Conv_1:

	m_auto_pad = str()
	m_dilations = list()
	m_group = int()
	m_kernel_shape = list()
	m_pads = list()
	m_strides = list()
	def __init__(self, _name: str, _tensor: dict, auto_pad=str(), dilations=list(), group=int(), kernel_shape=list(), pads=list(), strides=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_dilations = dilations
		self.m_group = group
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_strides = strides

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str, W: str, B: str):
		self.m_X = X
		self.m_W = W
		self.m_B = B

		return (self.tensor[self.m_Y])
