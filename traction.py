#!/usr/bin/env python

from math import *

steps_max=2**32

class StepNRow:
	def __init__(self, r_unfold_min, r_unfold_max, r_row_to_step, d_min, d_freilauf, d_wheel, l_step_pedal, l_step_grip):
		self.r_unfold_min=r_unfold_min
		self.r_unfold_max=r_unfold_max
		self.r_row_to_step=r_row_to_step
		self.d_min=d_min
		self.d_freilauf=d_freilauf
		self.d_wheel=d_wheel
		self.l_step_pedal=l_step_pedal
		self.l_step_grip=l_step_grip
		self.l_trip_step=0.0
		self.l_trip_wheel=0.0
		self.f_left=complex(0.0, 0.0)
		self.f_right=complex(0.0, 0.0)

	def run(self, steps=0):
		if steps<1:
			steps=steps_max
		for i in range(steps):
			self.l_trip_step += (pi/2.0)*float(i)
			t_left=sin(self.l_trip_step)
			t_right=sin(self.l_trip_step+(pi/2.0))
			v_left=sin(self.l_trip_step)
			v_right=sin(self.l_trip_step+(pi/2.0))
			f_left=complex(v_left,t_left)
			f_right=complex(v_right,t_right)
			print abs(f_left), abs(f_right)
		#p_vct_left
		#p_vct_right

	def set_thrust(self, f_thrust):
		self.f_thrust=f_thrust
	
	def set_drag(self, f_drag):
		self.f_drag=f_drag


# l_...-values in mm
# d_...-values in mm
# f_...-values in N
# t_...-values in Nm
# r_...-values are ratios
snr=StepNRow(0.6, 5.0, 1.5, 10.0, 120.0, 620.0,  500.0, 500.0)
snr.set_thrust(40.0)
snr.set_drag(4.0)
snr.run(10)
snr.set_thrust(40.0)
snr.set_drag(40.0)
snr.run(20)


