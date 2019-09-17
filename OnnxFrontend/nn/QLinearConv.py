from __future__ import absolute_import
from __future__ import division
import numpy as np

class QLinearConv_10:

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

	def output(self, y=str()):
		self.m_y = y


	def __call__(self, x=str(), x_scale=str(), x_zero_point=str(), w=str(), w_scale=str(), w_zero_point=str(), y_scale=str(), y_zero_point=str(), B=str()):
		self.m_x = x
		self.m_x_scale = x_scale
		self.m_x_zero_point = x_zero_point
		self.m_w = w
		self.m_w_scale = w_scale
		self.m_w_zero_point = w_zero_point
		self.m_y_scale = y_scale
		self.m_y_zero_point = y_zero_point
		self.m_B = B

		return (self.tensor[self.m_y])
