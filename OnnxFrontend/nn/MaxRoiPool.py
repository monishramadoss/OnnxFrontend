import numpy as np

class MaxRoiPool_1:

	pooled_shape = m_list()
	spatial_scale = m_float()
	def __init__(self, _name: str, pooled_shape: list, spatial_scale: float):
		self.name = _name
		self.m_pooled_shape = pooled_shape
		self.m_spatial_scale = spatial_scale

	def __call__(self, X: str, rois: str):
		 return Y
