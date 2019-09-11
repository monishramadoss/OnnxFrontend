import numpy as np

class Imputer_1:

	imputed_value_floats = m_list()
	imputed_value_int64s = m_list()
	replaced_value_float = m_float()
	replaced_value_int64 = m_int()
	def __init__(self, _name: str, imputed_value_floats: list, imputed_value_int64s: list, replaced_value_float: float, replaced_value_int64: int):
		self.name = _name
		self.m_imputed_value_floats = imputed_value_floats
		self.m_imputed_value_int64s = imputed_value_int64s
		self.m_replaced_value_float = replaced_value_float
		self.m_replaced_value_int64 = replaced_value_int64

	def __call__(self, X: str):
		 return Y
