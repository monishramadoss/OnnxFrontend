import numpy as np
from __future__ import absolute_import
from __future__ import division

class TfIdfVectorizer_9:

	max_gram_length = m_int()
	max_skip_count = m_int()
	min_gram_length = m_int()
	mode = m_str()
	ngram_counts = m_list()
	ngram_indexes = m_list()
	pool_int64s = m_list()
	pool_strings = m_list()
	weights = m_list()
	def __init__(self, _name: str, _tensor: dict, max_gram_length: int, max_skip_count: int, min_gram_length: int, mode: str, ngram_counts: list, ngram_indexes: list, pool_int64s: list, pool_strings: list, weights: list):
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

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
