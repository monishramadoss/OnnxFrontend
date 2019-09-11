import numpy as np

class RNN_1:

	activation_alpha = m_list()
	activation_beta = m_list()
	activations = m_list()
	clip = m_float()
	direction = m_str()
	hidden_size = m_int()
	output_sequence = m_int()
	def __init__(self, _name: str, activation_alpha: list, activation_beta: list, activations: list, clip: float, direction: str, hidden_size: int, output_sequence: int):
		self.name = _name
		self.m_activation_alpha = activation_alpha
		self.m_activation_beta = activation_beta
		self.m_activations = activations
		self.m_clip = clip
		self.m_direction = direction
		self.m_hidden_size = hidden_size
		self.m_output_sequence = output_sequence

	def __call__(self, X: str, W: str, R: str, B: str, sequence_lens: str, initial_h: str):
		 return Y, Y_h


class RNN_7:

	activation_alpha = m_list()
	activation_beta = m_list()
	activations = m_list()
	clip = m_float()
	direction = m_str()
	hidden_size = m_int()
	def __init__(self, _name: str, activation_alpha: list, activation_beta: list, activations: list, clip: float, direction: str, hidden_size: int):
		self.name = _name
		self.m_activation_alpha = activation_alpha
		self.m_activation_beta = activation_beta
		self.m_activations = activations
		self.m_clip = clip
		self.m_direction = direction
		self.m_hidden_size = hidden_size

	def __call__(self, X: str, W: str, R: str, B: str, sequence_lens: str, initial_h: str):
		 return Y, Y_h
