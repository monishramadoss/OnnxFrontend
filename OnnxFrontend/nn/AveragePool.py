from __future__ import absolute_import
from __future__ import division
import numpy as np

class AveragePool_1:

	m_auto_pad = str()
	m_kernel_shape = list()
	m_pads = list()
	m_strides = list()
	def __init__(self, _name: str, _tensor: dict, auto_pad=str(), kernel_shape=list(), pads=list(), strides=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_strides = strides

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])


class AveragePool_7:

	m_auto_pad = str()
	m_count_include_pad = int()
	m_kernel_shape = list()
	m_pads = list()
	m_strides = list()
	def __init__(self, _name: str, _tensor: dict, auto_pad=str(), count_include_pad=int(), kernel_shape=list(), pads=list(), strides=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_count_include_pad = count_include_pad
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_strides = strides

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])


class AveragePool_10:

	m_auto_pad = str()
	m_ceil_mode = int()
	m_count_include_pad = int()
	m_kernel_shape = list()
	m_pads = list()
	m_strides = list()
	def __init__(self, _name: str, _tensor: dict, auto_pad=str(), ceil_mode=int(), count_include_pad=int(), kernel_shape=list(), pads=list(), strides=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_ceil_mode = ceil_mode
		self.m_count_include_pad = count_include_pad
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_strides = strides

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
