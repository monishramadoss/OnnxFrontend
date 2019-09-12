import numpy as np
from __future__ import absolute_import
from __future__ import division

class LSTM_1:

	activation_alpha = m_list()
	activation_beta = m_list()
	activations = m_list()
	clip = m_float()
	direction = m_str()
	hidden_size = m_int()
	input_forget = m_int()
	output_sequence = m_int()
	def __init__(self, _name: str, _tensor: dict, activation_alpha: list, activation_beta: list, activations: list, clip: float, direction: str, hidden_size: int, input_forget: int, output_sequence: int):
		self.name = _name
		self.tensor = _tensor
		self.m_activation_alpha = activation_alpha
		self.m_activation_beta = activation_beta
		self.m_activations = activations
		self.m_clip = clip
		self.m_direction = direction
		self.m_hidden_size = hidden_size
		self.m_input_forget = input_forget
		self.m_output_sequence = output_sequence

	def __call__(self, X: str, W: str, R: str, B: str, sequence_lens: str, initial_h: str, initial_c: str, P: str):
		input = (self.tensor[X], self.tensor[W], self.tensor[R], self.tensor[B], self.tensor[sequence_lens], self.tensor[initial_h], self.tensor[initial_c], self.tensor[P])
		return self.tensor[Y], self.tensor[Y_h], self.tensor[Y_c]


class LSTM_7:

	activation_alpha = m_list()
	activation_beta = m_list()
	activations = m_list()
	clip = m_float()
	direction = m_str()
	hidden_size = m_int()
	input_forget = m_int()
	def __init__(self, _name: str, _tensor: dict, activation_alpha: list, activation_beta: list, activations: list, clip: float, direction: str, hidden_size: int, input_forget: int):
		self.name = _name
		self.tensor = _tensor
		self.m_activation_alpha = activation_alpha
		self.m_activation_beta = activation_beta
		self.m_activations = activations
		self.m_clip = clip
		self.m_direction = direction
		self.m_hidden_size = hidden_size
		self.m_input_forget = input_forget

	def __call__(self, X: str, W: str, R: str, B: str, sequence_lens: str, initial_h: str, initial_c: str, P: str):
		input = (self.tensor[X], self.tensor[W], self.tensor[R], self.tensor[B], self.tensor[sequence_lens], self.tensor[initial_h], self.tensor[initial_c], self.tensor[P])
		return self.tensor[Y], self.tensor[Y_h], self.tensor[Y_c]
