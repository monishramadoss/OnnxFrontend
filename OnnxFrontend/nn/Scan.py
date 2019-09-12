import numpy as np
from __future__ import absolute_import
from __future__ import division

class Scan_8:

	body = m_list()
	directions = m_list()
	num_scan_inputs = m_int()
	def __init__(self, _name: str, _tensor: dict, body: list, directions: list, num_scan_inputs: int):
		self.name = _name
		self.tensor = _tensor
		self.m_body = body
		self.m_directions = directions
		self.m_num_scan_inputs = num_scan_inputs

	def __call__(self, sequence_lens: str, initial_state_and_scan_inputs: str):
		input = (self.tensor[sequence_lens], self.tensor[initial_state_and_scan_inputs])
		return self.tensor[final_state_and_scan_outputs]


class Scan_9:

	body = m_list()
	num_scan_inputs = m_int()
	scan_input_axes = m_list()
	scan_input_directions = m_list()
	scan_output_axes = m_list()
	scan_output_directions = m_list()
	def __init__(self, _name: str, _tensor: dict, body: list, num_scan_inputs: int, scan_input_axes: list, scan_input_directions: list, scan_output_axes: list, scan_output_directions: list):
		self.name = _name
		self.tensor = _tensor
		self.m_body = body
		self.m_num_scan_inputs = num_scan_inputs
		self.m_scan_input_axes = scan_input_axes
		self.m_scan_input_directions = scan_input_directions
		self.m_scan_output_axes = scan_output_axes
		self.m_scan_output_directions = scan_output_directions

	def __call__(self, initial_state_and_scan_inputs: str):
		input = (self.tensor[initial_state_and_scan_inputs])
		return self.tensor[final_state_and_scan_outputs]
