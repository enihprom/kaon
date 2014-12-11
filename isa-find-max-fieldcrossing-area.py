#!/usr/bin/env python


class RepellSpring:
	def __init__(self, magnet1, magnet2):
		self.magnet1 = magnet1
		self.magnat2 = magnet2
	
	def apply_impulse(self, p):
		"""
		applies a linear collision impulse between the 2 magnets
		p	impuls vector where values > 0.0 are contracting
		and values < 0.0 are expanding forces
		"""
		self.force=p
	
	def force_between_bars(self):
		return (pi * mu0 / 4) * M**2 * r**4 * (1.0/x**2 + 1.0/(x+2.0*h)**2 - 2.0/(x+h)**2)

	def force_between_cylinders(self):
		return (pi * mu0 / 4) * M**2 * r**4 * (1.0/x**2 + 1.0/(x+h)**2 - 2.0/(x+h)**2)

	def force_between_poles(self):
		return (mu * qm1 * qm2) / (4.0 * pi * r**2)

	def force_between_surfaces_by_field(self):
		return (mu0 * H**2 * A) / 2
	
	def force_between_surfaces_by_flux(self):
		return (B**2 * A) / (2 * mu0)
	
	def get_field_vector(self, r, z):
		if r=0.0:
			return (0,0,force_between)


