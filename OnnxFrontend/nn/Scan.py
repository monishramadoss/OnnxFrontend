from __future__ import absolute_import
from __future__ import division
import numpy as np

class Scan_8:

	m_body = list()
	m_directions = list()
	m_num_scan_inputs = int()
	def __init__(self, _name: str, _tensor: dict, body=list(), directions=list(), num_scan_inputs=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_body = body
		self.m_directions = directions
		self.m_num_scan_inputs = num_scan_inputs

	def output(self, final_state_and_scan_outputs=str()):
		self.m_final_state_and_scan_outputs = final_state_and_scan_outputs


	def __call__(self, sequence_lens=str(), initial_state_and_scan_inputs=str()):
		self.m_sequence_lens = sequence_lens
		self.m_initial_state_and_scan_inputs = initial_state_and_scan_inputs

		return (self.tensor[self.m_final_state_and_scan_outputs])


class Scan_9:

	m_body = list()
	m_num_scan_inputs = int()
	m_scan_input_axes = list()
	m_scan_input_directions = list()
	m_scan_output_axes = list()
	m_scan_output_directions = list()
	def __init__(self, _name: str, _tensor: dict, body=list(), num_scan_inputs=int(), scan_input_axes=list(), scan_input_directions=list(), scan_output_axes=list(), scan_output_directions=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_body = body
		self.m_num_scan_inputs = num_scan_inputs
		self.m_scan_input_axes = scan_input_axes
		self.m_scan_input_directions = scan_input_directions
		self.m_scan_output_axes = scan_output_axes
		self.m_scan_output_directions = scan_output_directions

	def output(self, final_state_and_scan_outputs=str()):
		self.m_final_state_and_scan_outputs = final_state_and_scan_outputs


	def __call__(self, initial_state_and_scan_inputs=str()):
		self.m_initial_state_and_scan_inputs = initial_state_and_scan_inputs

		return #(self.tensor[self.m_final_state_and_scan_outputs])
