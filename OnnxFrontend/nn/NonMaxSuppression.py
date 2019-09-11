import numpy as np

class NonMaxSuppression_10:

	center_point_box = m_int()
	def __init__(self, _name: str, center_point_box: int):
		self.name = _name
		self.m_center_point_box = center_point_box

	def __call__(self, boxes: str, scores: str, max_output_boxes_per_class: str, iou_threshold: str, score_threshold: str):
		 return selected_indices
