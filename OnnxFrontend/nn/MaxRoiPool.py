from __future__ import absolute_import
from __future__ import division
import numpy as np

class MaxRoiPool_1:

	m_pooled_shape = list()
	m_spatial_scale = float()
	def __init__(self, _name: str, _tensor: dict, pooled_shape=list(), spatial_scale=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_pooled_shape = pooled_shape
		self.m_spatial_scale = spatial_scale

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str, rois: str):
		self.m_X = X
		self.m_rois = rois

		return (self.tensor[self.m_Y])
