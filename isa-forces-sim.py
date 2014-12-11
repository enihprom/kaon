#!/usr/bin/env python

import math
import os
import sys
import magnets


class Conductor:
	def __init__(self, geometry_mesh)


class Material:
	def __init__(self,
			ferromagnetism, diamagnetism, paramagnetism,
			thermal_conductivity, electric_conductivity):
		self.ferromagnetism = ferromagnetism
		self.paramagnetism = paramagnetism - diamagnetism


class Wire:
	# 1-dimensional simplification of Conductor
	def __init__(self, waypoints=[[0.0,0.0,0.0], [1.0,1.0,1.0]], material)
		self.waypoints=waypoints
		self.material=material

	def expand_at(self, n, p):
		self.waypoints.insert(n, p)
	
	def find(self, p)
		for i in range(len(self.waypoints)):
			if p == self.waypoints[i]:
				return i
	
	def current_at(self, waypoint, offset):
		pass

	def apply_field(self, magnet):
		pass
	
