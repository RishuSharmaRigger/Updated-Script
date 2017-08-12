'''
grp = Select Animated Object or CTRL.
CtrlName = Fingers_L.Relax (Put ctrl name which have a attribute)
'''

import pymel.core as pm
def connectAttribute():
	grp = pm.ls(sl=True)
	pm.delete(grp,sc=True)
	CtrlName = "nurbsCircle1.Test"
	animCurve = pm.findKeyframe(grp[0],c=True)
	for i in range(len(animCurve)):
		connect = pm.connectAttr(CtrlName,animCurve[i]+".input")
	print "animCurve Connected...",
		
connectAttribute()


print 'test'
