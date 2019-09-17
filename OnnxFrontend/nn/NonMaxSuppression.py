from __future__ import absolute_import
from __future__ import division
import numpy as np

class NonMaxSuppression_10:

	m_center_point_box = int()
	def __init__(self, _name: str, _tensor: dict, center_point_box=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_center_point_box = center_point_box

	def output(self, selected_indices=str()):
		self.m_selected_indices = selected_indices


	def __call__(self, boxes=str(), scores=str(), max_output_boxes_per_class=str(), iou_threshold=str(), score_threshold=str()):
		self.m_boxes = boxes
		self.m_scores = scores
		self.m_max_output_boxes_per_class = max_output_boxes_per_class
		self.m_iou_threshold = iou_threshold
		self.m_score_threshold = score_threshold

		return (self.tensor[self.m_selected_indices])
