import numpy as np
from __future__ import absolute_import
from __future__ import division

class EyeLike_9:

	dtype = m_int()
	k = m_int()
	def __init__(self, _name: str, _tensor: dict, dtype: int, k: int):
		self.name = _name
		self.tensor = _tensor
		self.m_dtype = dtype
		self.m_k = k

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
