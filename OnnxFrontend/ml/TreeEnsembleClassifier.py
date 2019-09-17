from __future__ import absolute_import
from __future__ import division
import numpy as np

class TreeEnsembleClassifier_1:

	m_base_values = list()
	m_class_ids = list()
	m_class_nodeids = list()
	m_class_treeids = list()
	m_class_weights = list()
	m_classlabels_int64s = list()
	m_classlabels_strings = list()
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
	def __init__(self, _name: str, _tensor: dict, base_values=list(), class_ids=list(), class_nodeids=list(), class_treeids=list(), class_weights=list(), classlabels_int64s=list(), classlabels_strings=list(), nodes_falsenodeids=list(), nodes_featureids=list(), nodes_hitrates=list(), nodes_missing_value_tracks_true=list(), nodes_modes=list(), nodes_nodeids=list(), nodes_treeids=list(), nodes_truenodeids=list(), nodes_values=list(), post_transform=str()):
		self.name = _name
		self.tensor = _tensor
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

	def output(self, Y=str(), Z=str()):
		self.m_Y = Y
		self.m_Z = Z


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y], self.tensor[self.m_Z])
