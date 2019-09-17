from __future__ import absolute_import
from __future__ import division
import numpy as np

class TfIdfVectorizer_9:

	m_max_gram_length = int()
	m_max_skip_count = int()
	m_min_gram_length = int()
	m_mode = str()
	m_ngram_counts = list()
	m_ngram_indexes = list()
	m_pool_int64s = list()
	m_pool_strings = list()
	m_weights = list()
	def __init__(self, _name: str, _tensor: dict, max_gram_length=int(), max_skip_count=int(), min_gram_length=int(), mode=str(), ngram_counts=list(), ngram_indexes=list(), pool_int64s=list(), pool_strings=list(), weights=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_max_gram_length = max_gram_length
		self.m_max_skip_count = max_skip_count
		self.m_min_gram_length = min_gram_length
		self.m_mode = mode
		self.m_ngram_counts = ngram_counts
		self.m_ngram_indexes = ngram_indexes
		self.m_pool_int64s = pool_int64s
		self.m_pool_strings = pool_strings
		self.m_weights = weights

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
