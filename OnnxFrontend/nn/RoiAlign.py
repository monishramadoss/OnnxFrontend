import numpy as np

class RoiAlign_10:

	mode = m_str()
	output_height = m_int()
	output_width = m_int()
	sampling_ratio = m_int()
	spatial_scale = m_float()
	def __init__(self, _name: str, mode: str, output_height: int, output_width: int, sampling_ratio: int, spatial_scale: float):
		self.name = _name
		self.m_mode = mode
		self.m_output_height = output_height
		self.m_output_width = output_width
		self.m_sampling_ratio = sampling_ratio
		self.m_spatial_scale = spatial_scale

	def __call__(self, X: str, rois: str, batch_indices: str):
		 return Y
