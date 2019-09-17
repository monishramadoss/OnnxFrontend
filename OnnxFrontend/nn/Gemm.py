from __future__ import absolute_import
from __future__ import division
import numpy as np

class Gemm_1:

	m_alpha = float()
	m_beta = float()
	m_broadcast = int()
	m_transA = int()
	m_transB = int()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), beta=float(), broadcast=int(), transA=int(), transB=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_broadcast = broadcast
		self.m_transA = transA
		self.m_transB = transB

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, A=str(), B=str(), C=str()):
		self.m_A = A
		self.m_B = B
		self.m_C = C

		return (self.tensor[self.m_Y])


class Gemm_6:

	m_alpha = float()
	m_beta = float()
	m_broadcast = int()
	m_transA = int()
	m_transB = int()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), beta=float(), broadcast=int(), transA=int(), transB=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_broadcast = broadcast
		self.m_transA = transA
		self.m_transB = transB

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, A=str(), B=str(), C=str()):
		self.m_A = A
		self.m_B = B
		self.m_C = C

		return (self.tensor[self.m_Y])


class Gemm_7:

	m_alpha = float()
	m_beta = float()
	m_transA = int()
	m_transB = int()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), beta=float(), transA=int(), transB=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_transA = transA
		self.m_transB = transB

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, A=str(), B=str(), C=str()):
		self.m_A = A
		self.m_B = B
		self.m_C = C

		return (self.tensor[self.m_Y])


class Gemm_9:

	m_alpha = float()
	m_beta = float()
	m_transA = int()
	m_transB = int()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), beta=float(), transA=int(), transB=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_beta = beta
		self.m_transA = transA
		self.m_transB = transB

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, A=str(), B=str(), C=str()):
		self.m_A = A
		self.m_B = B
		self.m_C = C

		return (self.tensor[self.m_Y])
