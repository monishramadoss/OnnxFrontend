import numpy as np
from __future__ import absolute_import
from __future__ import division

class TreeEnsembleRegressor_1:

	aggregate_function = m_str()
	base_values = m_list()
	n_targets = m_int()
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
	target_ids = m_list()
	target_nodeids = m_list()
	target_treeids = m_list()
	target_weights = m_list()
	def __init__(self, _name: str, _tensor: dict, aggregate_function: str, base_values: list, n_targets: int, nodes_falsenodeids: list, nodes_featureids: list, nodes_hitrates: list, nodes_missing_value_tracks_true: list, nodes_modes: list, nodes_nodeids: list, nodes_treeids: list, nodes_truenodeids: list, nodes_values: list, post_transform: str, target_ids: list, target_nodeids: list, target_treeids: list, target_weights: list):
		self.name = _name
		self.tensor = _tensor
		self.m_aggregate_function = aggregate_function
		self.m_base_values = base_values
		self.m_n_targets = n_targets
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
		self.m_target_ids = target_ids
		self.m_target_nodeids = target_nodeids
		self.m_target_treeids = target_treeids
		self.m_target_weights = target_weights

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
