from __future__ import absolute_import
from __future__ import division
import numpy as np

class Imputer_1:

	m_imputed_value_floats = list()
	m_imputed_value_int64s = list()
	m_replaced_value_float = float()
	m_replaced_value_int64 = int()
	def __init__(self, _name: str, _tensor: dict, imputed_value_floats=list(), imputed_value_int64s=list(), replaced_value_float=float(), replaced_value_int64=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_imputed_value_floats = imputed_value_floats
		self.m_imputed_value_int64s = imputed_value_int64s
		self.m_replaced_value_float = replaced_value_float
		self.m_replaced_value_int64 = replaced_value_int64

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
