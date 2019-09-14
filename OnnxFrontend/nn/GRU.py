from __future__ import absolute_import
from __future__ import division
import numpy as np

class GRU_1:

	m_activation_alpha = list()
	m_activation_beta = list()
	m_activations = list()
	m_clip = float()
	m_direction = str()
	m_hidden_size = int()
	m_output_sequence = int()
	def __init__(self, _name: str, _tensor: dict, activation_alpha=list(), activation_beta=list(), activations=list(), clip=float(), direction=str(), hidden_size=int(), output_sequence=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_activation_alpha = activation_alpha
		self.m_activation_beta = activation_beta
		self.m_activations = activations
		self.m_clip = clip
		self.m_direction = direction
		self.m_hidden_size = hidden_size
		self.m_output_sequence = output_sequence

	def output(self, Y, Y_h):
		self.m_Y = Y
		self.m_Y_h = Y_h


	def __call__(self, X: str, W: str, R: str, B: str, sequence_lens: str, initial_h: str):
		self.m_X = X
		self.m_W = W
		self.m_R = R
		self.m_B = B
		self.m_sequence_lens = sequence_lens
		self.m_initial_h = initial_h

		return (self.tensor[self.m_Y, self.m_Y_h])


class GRU_3:

	m_activation_alpha = list()
	m_activation_beta = list()
	m_activations = list()
	m_clip = float()
	m_direction = str()
	m_hidden_size = int()
	m_linear_before_reset = int()
	m_output_sequence = int()
	def __init__(self, _name: str, _tensor: dict, activation_alpha=list(), activation_beta=list(), activations=list(), clip=float(), direction=str(), hidden_size=int(), linear_before_reset=int(), output_sequence=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_activation_alpha = activation_alpha
		self.m_activation_beta = activation_beta
		self.m_activations = activations
		self.m_clip = clip
		self.m_direction = direction
		self.m_hidden_size = hidden_size
		self.m_linear_before_reset = linear_before_reset
		self.m_output_sequence = output_sequence

	def output(self, Y, Y_h):
		self.m_Y = Y
		self.m_Y_h = Y_h


	def __call__(self, X: str, W: str, R: str, B: str, sequence_lens: str, initial_h: str):
		self.m_X = X
		self.m_W = W
		self.m_R = R
		self.m_B = B
		self.m_sequence_lens = sequence_lens
		self.m_initial_h = initial_h

		return (self.tensor[self.m_Y, self.m_Y_h])


class GRU_7:

	m_activation_alpha = list()
	m_activation_beta = list()
	m_activations = list()
	m_clip = float()
	m_direction = str()
	m_hidden_size = int()
	m_linear_before_reset = int()
	def __init__(self, _name: str, _tensor: dict, activation_alpha=list(), activation_beta=list(), activations=list(), clip=float(), direction=str(), hidden_size=int(), linear_before_reset=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_activation_alpha = activation_alpha
		self.m_activation_beta = activation_beta
		self.m_activations = activations
		self.m_clip = clip
		self.m_direction = direction
		self.m_hidden_size = hidden_size
		self.m_linear_before_reset = linear_before_reset

	def output(self, Y, Y_h):
		self.m_Y = Y
		self.m_Y_h = Y_h


	def __call__(self, X: str, W: str, R: str, B: str, sequence_lens: str, initial_h: str):
		self.m_X = X
		self.m_W = W
		self.m_R = R
		self.m_B = B
		self.m_sequence_lens = sequence_lens
		self.m_initial_h = initial_h

		return (self.tensor[self.m_Y, self.m_Y_h])
