import numpy as np

class CastMap_1:

	cast_to = m_str()
	map_form = m_str()
	max_map = m_int()
	def __init__(self, _name: str, cast_to: str, map_form: str, max_map: int):
		self.name = _name
		self.m_cast_to = cast_to
		self.m_map_form = map_form
		self.m_max_map = max_map

	def __call__(self, X: str):
		 return Y
