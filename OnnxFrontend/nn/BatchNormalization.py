from __future__ import absolute_import
from __future__ import division
import numpy as np

class BatchNormalization_1:

	m_consumed_inputs = list()
	m_epsilon = float()
	m_is_test = int()
	m_momentum = float()
	m_spatial = int()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs=list(), epsilon=float(), is_test=int(), momentum=float(), spatial=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_epsilon = epsilon
		self.m_is_test = is_test
		self.m_momentum = momentum
		self.m_spatial = spatial

	def output(self, Y=str(), mean=str(), var=str(), saved_mean=str(), saved_var=str()):
		self.m_Y = Y
		self.m_mean = mean
		self.m_var = var
		self.m_saved_mean = saved_mean
		self.m_saved_var = saved_var


	def __call__(self, X=str(), scale=str(), B=str(), mean=str(), var=str()):
		self.m_X = X
		self.m_scale = scale
		self.m_B = B
		self.m_mean = mean
		self.m_var = var

		return (self.tensor[self.m_Y], self.tensor[self.m_mean], self.tensor[self.m_var], self.tensor[self.m_saved_mean], self.tensor[self.m_saved_var])


class BatchNormalization_6:

	m_epsilon = float()
	m_is_test = int()
	m_momentum = float()
	m_spatial = int()
	def __init__(self, _name: str, _tensor: dict, epsilon=float(), is_test=int(), momentum=float(), spatial=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_epsilon = epsilon
		self.m_is_test = is_test
		self.m_momentum = momentum
		self.m_spatial = spatial

	def output(self, Y=str(), mean=str(), var=str(), saved_mean=str(), saved_var=str()):
		self.m_Y = Y
		self.m_mean = mean
		self.m_var = var
		self.m_saved_mean = saved_mean
		self.m_saved_var = saved_var


	def __call__(self, X=str(), scale=str(), B=str(), mean=str(), var=str()):
		self.m_X = X
		self.m_scale = scale
		self.m_B = B
		self.m_mean = mean
		self.m_var = var

		return (self.tensor[self.m_Y], self.tensor[self.m_mean], self.tensor[self.m_var], self.tensor[self.m_saved_mean], self.tensor[self.m_saved_var])


class BatchNormalization_7:

	m_epsilon = float()
	m_momentum = float()
	m_spatial = int()
	def __init__(self, _name: str, _tensor: dict, epsilon=float(), momentum=float(), spatial=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_epsilon = epsilon
		self.m_momentum = momentum
		self.m_spatial = spatial

	def output(self, Y=str(), mean=str(), var=str(), saved_mean=str(), saved_var=str()):
		self.m_Y = Y
		self.m_mean = mean
		self.m_var = var
		self.m_saved_mean = saved_mean
		self.m_saved_var = saved_var


	def __call__(self, X=str(), scale=str(), B=str(), mean=str(), var=str()):
		self.m_X = X
		self.m_scale = scale
		self.m_B = B
		self.m_mean = mean
		self.m_var = var

		return (self.tensor[self.m_Y], self.tensor[self.m_mean], self.tensor[self.m_var], self.tensor[self.m_saved_mean], self.tensor[self.m_saved_var])


class BatchNormalization_9:

	m_epsilon = float()
	m_momentum = float()
	def __init__(self, _name: str, _tensor: dict, epsilon=float(), momentum=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_epsilon = epsilon
		self.m_momentum = momentum

	def output(self, Y=str(), mean=str(), var=str(), saved_mean=str(), saved_var=str()):
		self.m_Y = Y
		self.m_mean = mean
		self.m_var = var
		self.m_saved_mean = saved_mean
		self.m_saved_var = saved_var


	def __call__(self, X=str(), scale=str(), B=str(), mean=str(), var=str()):
		self.m_X = X
		self.m_scale = scale
		self.m_B = B
		self.m_mean = mean
		self.m_var = var

		return (self.tensor[self.m_Y], self.tensor[self.m_mean], self.tensor[self.m_var], self.tensor[self.m_saved_mean], self.tensor[self.m_saved_var])
