import bpy
import bpy.data
import bpy.ops
import bpy.context
import bpygenerators

C = bpy.context
D = bpy.context

class GData:
    pass

def demands_to_geometry(ua, ub, d_max, l_max, phi_ad):
    g=gdata()
    g.ta=phi_ad

    return g

""" return  (p_start, p_end) indices of the circular aligned
            vertices at each side """
def generate_inner_surface(gdata):
    for i in range(l):
        z1a=i;
        r1a=g/2
        t1a=+0+0
        z2a=i;
        r2a=g/2
        t2a=+rad(120)+0
        z3a=i;
        r3a=g/2
        t3a=+rad(240)+0
        z1b=i;
        r1b=g/2
        t1b=+0+gdata.ta # addendum surface phi_0x+
        z2b=i;
        r2b=g/2
        t2b=+0+rad(120)+gdata.ta
        z3b=i;
        r3b=g/2
        t3b=+0+rad(240)+gdata.ta
        #TODO

def generate_outer_surface(gdata)
    pass #TODO

def generate_wormtube(gdata):
    inner=generate_inner_surface(gdata)
    outer

def generate_wormtube_direct(x,y,z,l,d,wi,wo,pis,pos,pie,poe):
    g=gdata()
    g.x=x
    g.y=y
    g.z=z
    g.l=l
    g.d=d
    g.wi=wi
    g.wo=wo
    g.pis=pis
    g.pos=pos
    g.pie=pie
    g.poe=poe

