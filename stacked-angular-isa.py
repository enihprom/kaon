#!/usr/bin/env python


class Jaws:
	def __init__(self, l, n, d, m):
		"""
		l	length of the jaw bone
		n	number of "teeth" (equipolar repellant pairs)
		d  spacin between each magnet pair
		m  magnet object
		"""
		self.l=l
		self.n=n
		self.d=d
		self.m=m
	
	def apply_weight_force(self, F, at_l):
		pass

