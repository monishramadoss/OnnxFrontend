import numpy as np
from __future__ import absolute_import
from __future__ import division

class NonMaxSuppression_10:

	center_point_box = m_int()
	def __init__(self, _name: str, _tensor: dict, center_point_box: int):
		self.name = _name
		self.tensor = _tensor
		self.m_center_point_box = center_point_box

	def __call__(self, boxes: str, scores: str, max_output_boxes_per_class: str, iou_threshold: str, score_threshold: str):
		input = (self.tensor[boxes], self.tensor[scores], self.tensor[max_output_boxes_per_class], self.tensor[iou_threshold], self.tensor[score_threshold])
		return self.tensor[selected_indices]
