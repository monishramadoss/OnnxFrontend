import numpy as np

class TreeEnsembleClassifier_1:

	base_values = m_list()
	class_ids = m_list()
	class_nodeids = m_list()
	class_treeids = m_list()
	class_weights = m_list()
	classlabels_int64s = m_list()
	classlabels_strings = m_list()
	nodes_falsenodeids = m_list()
	nodes_featureids = m_list()
	nodes_hitrates = m_list()
	nodes_missing_value_tracks_true = m_list()
	nodes_modes = m_list()
	nodes_nodeids = m_list()
	nodes_treeids = m_list()
	nodes_truenodeids = m_list()
	nodes_values = m_list()
	post_transform = m_str()
	def __init__(self, _name: str, base_values: list, class_ids: list, class_nodeids: list, class_treeids: list, class_weights: list, classlabels_int64s: list, classlabels_strings: list, nodes_falsenodeids: list, nodes_featureids: list, nodes_hitrates: list, nodes_missing_value_tracks_true: list, nodes_modes: list, nodes_nodeids: list, nodes_treeids: list, nodes_truenodeids: list, nodes_values: list, post_transform: str):
		self.name = _name
		self.m_base_values = base_values
		self.m_class_ids = class_ids
		self.m_class_nodeids = class_nodeids
		self.m_class_treeids = class_treeids
		self.m_class_weights = class_weights
		self.m_classlabels_int64s = classlabels_int64s
		self.m_classlabels_strings = classlabels_strings
		self.m_nodes_falsenodeids = nodes_falsenodeids
		self.m_nodes_featureids = nodes_featureids
		self.m_nodes_hitrates = nodes_hitrates
		self.m_nodes_missing_value_tracks_true = nodes_missing_value_tracks_true
		self.m_nodes_modes = nodes_modes
		self.m_nodes_nodeids = nodes_nodeids
		self.m_nodes_treeids = nodes_treeids
		self.m_nodes_truenodeids = nodes_truenodeids
		self.m_nodes_values = nodes_values
		self.m_post_transform = post_transform

	def __call__(self, X: str):
		 return Y, Z
