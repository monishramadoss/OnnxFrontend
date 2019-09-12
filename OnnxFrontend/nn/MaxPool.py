import numpy as np
from __future__ import absolute_import
from __future__ import division

class MaxPool_1:

	auto_pad = m_str()
	kernel_shape = m_list()
	pads = m_list()
	strides = m_list()
	def __init__(self, _name: str, _tensor: dict, auto_pad: str, kernel_shape: list, pads: list, strides: list):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_strides = strides

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]


class MaxPool_8:

	auto_pad = m_str()
	kernel_shape = m_list()
	pads = m_list()
	storage_order = m_int()
	strides = m_list()
	def __init__(self, _name: str, _tensor: dict, auto_pad: str, kernel_shape: list, pads: list, storage_order: int, strides: list):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_storage_order = storage_order
		self.m_strides = strides

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y], self.tensor[Indices]


class MaxPool_10:

	auto_pad = m_str()
	ceil_mode = m_int()
	dilations = m_list()
	kernel_shape = m_list()
	pads = m_list()
	storage_order = m_int()
	strides = m_list()
	def __init__(self, _name: str, _tensor: dict, auto_pad: str, ceil_mode: int, dilations: list, kernel_shape: list, pads: list, storage_order: int, strides: list):
		self.name = _name
		self.tensor = _tensor
		self.m_auto_pad = auto_pad
		self.m_ceil_mode = ceil_mode
		self.m_dilations = dilations
		self.m_kernel_shape = kernel_shape
		self.m_pads = pads
		self.m_storage_order = storage_order
		self.m_strides = strides

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y], self.tensor[Indices]
