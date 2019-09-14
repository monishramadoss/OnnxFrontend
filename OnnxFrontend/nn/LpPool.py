from __future__ import absolute_import
from __future__ import division
import numpy as np

class LpPool_1:

	m_auto_pad = str()
	m_kernel_shape = list()
	m_p = float()
	m_pads = list()
	m_strides = list()
	def __init__(self, _name: str, _tensor: dict, auto_pad=str(), kernel_shape=list(), p=float(), pads=list(), strides=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_kernel_shape = kernel_shape
		self.m_p = p
		self.m_pads = pads
		self.m_strides = strides

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])


class LpPool_2:

	m_auto_pad = str()
	m_kernel_shape = list()
	m_p = int()
	m_pads = list()
	m_strides = list()
	def __init__(self, _name: str, _tensor: dict, auto_pad=str(), kernel_shape=list(), p=int(), pads=list(), strides=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_kernel_shape = kernel_shape
		self.m_p = p
		self.m_pads = pads
		self.m_strides = strides

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])
