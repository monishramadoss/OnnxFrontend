from __future__ import absolute_import
from __future__ import division
import numpy as np

class TreeEnsembleRegressor_1:

	m_aggregate_function = str()
	m_base_values = list()
	m_n_targets = int()
	m_nodes_falsenodeids = list()
	m_nodes_featureids = list()
	m_nodes_hitrates = list()
	m_nodes_missing_value_tracks_true = list()
	m_nodes_modes = list()
	m_nodes_nodeids = list()
	m_nodes_treeids = list()
	m_nodes_truenodeids = list()
	m_nodes_values = list()
	m_post_transform = str()
	m_target_ids = list()
	m_target_nodeids = list()
	m_target_treeids = list()
	m_target_weights = list()
	def __init__(self, _name: str, _tensor: dict, aggregate_function=str(), base_values=list(), n_targets=int(), nodes_falsenodeids=list(), nodes_featureids=list(), nodes_hitrates=list(), nodes_missing_value_tracks_true=list(), nodes_modes=list(), nodes_nodeids=list(), nodes_treeids=list(), nodes_truenodeids=list(), nodes_values=list(), post_transform=str(), target_ids=list(), target_nodeids=list(), target_treeids=list(), target_weights=list()):
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

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])
