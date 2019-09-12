import numpy as np
from __future__ import absolute_import
from __future__ import division

class BatchNormalization_1:

	consumed_inputs = m_list()
	epsilon = m_float()
	is_test = m_int()
	momentum = m_float()
	spatial = m_int()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs: list, epsilon: float, is_test: int, momentum: float, spatial: int):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_epsilon = epsilon
		self.m_is_test = is_test
		self.m_momentum = momentum
		self.m_spatial = spatial

	def __call__(self, X: str, scale: str, B: str, mean: str, var: str):
		input = (self.tensor[X], self.tensor[scale], self.tensor[B], self.tensor[mean], self.tensor[var])
		return self.tensor[Y], self.tensor[mean], self.tensor[var], self.tensor[saved_mean], self.tensor[saved_var]


class BatchNormalization_6:

	epsilon = m_float()
	is_test = m_int()
	momentum = m_float()
	spatial = m_int()
	def __init__(self, _name: str, _tensor: dict, epsilon: float, is_test: int, momentum: float, spatial: int):
		self.name = _name
		self.tensor = _tensor
		self.m_epsilon = epsilon
		self.m_is_test = is_test
		self.m_momentum = momentum
		self.m_spatial = spatial

	def __call__(self, X: str, scale: str, B: str, mean: str, var: str):
		input = (self.tensor[X], self.tensor[scale], self.tensor[B], self.tensor[mean], self.tensor[var])
		return self.tensor[Y], self.tensor[mean], self.tensor[var], self.tensor[saved_mean], self.tensor[saved_var]


class BatchNormalization_7:

	epsilon = m_float()
	momentum = m_float()
	spatial = m_int()
	def __init__(self, _name: str, _tensor: dict, epsilon: float, momentum: float, spatial: int):
		self.name = _name
		self.tensor = _tensor
		self.m_epsilon = epsilon
		self.m_momentum = momentum
		self.m_spatial = spatial

	def __call__(self, X: str, scale: str, B: str, mean: str, var: str):
		input = (self.tensor[X], self.tensor[scale], self.tensor[B], self.tensor[mean], self.tensor[var])
		return self.tensor[Y], self.tensor[mean], self.tensor[var], self.tensor[saved_mean], self.tensor[saved_var]


class BatchNormalization_9:

	epsilon = m_float()
	momentum = m_float()
	def __init__(self, _name: str, _tensor: dict, epsilon: float, momentum: float):
		self.name = _name
		self.tensor = _tensor
		self.m_epsilon = epsilon
		self.m_momentum = momentum

	def __call__(self, X: str, scale: str, B: str, mean: str, var: str):
		input = (self.tensor[X], self.tensor[scale], self.tensor[B], self.tensor[mean], self.tensor[var])
		return self.tensor[Y], self.tensor[mean], self.tensor[var], self.tensor[saved_mean], self.tensor[saved_var]
