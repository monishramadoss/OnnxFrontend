import numpy as np
from __future__ import absolute_import
from __future__ import division

class MaxRoiPool_1:

	pooled_shape = m_list()
	spatial_scale = m_float()
	def __init__(self, _name: str, _tensor: dict, pooled_shape: list, spatial_scale: float):
		self.name = _name
		self.tensor = _tensor
		self.m_pooled_shape = pooled_shape
		self.m_spatial_scale = spatial_scale

	def __call__(self, X: str, rois: str):
		input = (self.tensor[X], self.tensor[rois])
		return self.tensor[Y]
