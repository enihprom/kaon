#!/usr/bin/env python

class BaseMagnet(object):
	def __init__(self, tesla, theta, phi):
		#todo
		#B0, A, L, R, x
		#move(x,y)
		#adjust(th,ph)
		#...

class Magnet(BaseMagnet):
	def __init__(self, tesla, theta, phi):
		super(self)
		self.scale(tesla)
		self.move(theta, phi)
	
	def move(self, theta, phi):
		self.theta=theta
		self.phi=phi
	
	def scale(self, tesla)
		self.tesla=tesla

class StaticMagnet(Magnet):
	pass

