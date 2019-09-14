from __future__ import absolute_import
from __future__ import division
import numpy as np

class RoiAlign_10:

	m_mode = str()
	m_output_height = int()
	m_output_width = int()
	m_sampling_ratio = int()
	m_spatial_scale = float()
	def __init__(self, _name: str, _tensor: dict, mode=str(), output_height=int(), output_width=int(), sampling_ratio=int(), spatial_scale=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_mode = mode
		self.m_output_height = output_height
		self.m_output_width = output_width
		self.m_sampling_ratio = sampling_ratio
		self.m_spatial_scale = spatial_scale

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str, rois: str, batch_indices: str):
		self.m_X = X
		self.m_rois = rois
		self.m_batch_indices = batch_indices

		return (self.tensor[self.m_Y])
