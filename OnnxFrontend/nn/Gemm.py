import numpy as np

class Gemm_1:

	alpha = m_float()
	beta = m_float()
	broadcast = m_int()
	transA = m_int()
	transB = m_int()
	def __init__(self, _name: str, alpha: float, beta: float, broadcast: int, transA: int, transB: int):
		self.name = _name
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_broadcast = broadcast
		self.m_transA = transA
		self.m_transB = transB

	def __call__(self, A: str, B: str, C: str):
		 return Y


class Gemm_6:

	alpha = m_float()
	beta = m_float()
	broadcast = m_int()
	transA = m_int()
	transB = m_int()
	def __init__(self, _name: str, alpha: float, beta: float, broadcast: int, transA: int, transB: int):
		self.name = _name
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_broadcast = broadcast
		self.m_transA = transA
		self.m_transB = transB

	def __call__(self, A: str, B: str, C: str):
		 return Y


class Gemm_7:

	alpha = m_float()
	beta = m_float()
	transA = m_int()
	transB = m_int()
	def __init__(self, _name: str, alpha: float, beta: float, transA: int, transB: int):
		self.name = _name
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_transA = transA
		self.m_transB = transB

	def __call__(self, A: str, B: str, C: str):
		 return Y


class Gemm_9:

	alpha = m_float()
	beta = m_float()
	transA = m_int()
	transB = m_int()
	def __init__(self, _name: str, alpha: float, beta: float, transA: int, transB: int):
		self.name = _name
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_transA = transA
		self.m_transB = transB

	def __call__(self, A: str, B: str, C: str):
		 return Y
