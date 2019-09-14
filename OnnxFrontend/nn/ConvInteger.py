from __future__ import absolute_import
from __future__ import division
import numpy as np

class ConvInteger_10:

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

	def output(self, y):
		self.m_y = y


	def __call__(self, x: str, w: str, x_zero_point: str, w_zero_point: str):
		self.m_x = x
		self.m_w = w
		self.m_x_zero_point = x_zero_point
		self.m_w_zero_point = w_zero_point

		return (self.tensor[self.m_y])
