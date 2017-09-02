#Script for Transfer Attribute.
import pymel.core as pm

def transferAttribute():
	obj = pm.ls(sl=True)
	if obj:
		allObj = ("A1","A2","A3","A4","A5","A13","A7","A8","A9","A10","A11")
		for i in range(len(obj)):
			getTrans = obj[i].translate.get()
			getRotate = obj[i].rotate.get()
			getScale = obj[i].scale.get()
			pm.setAttr(allObj[i]+".t",getTrans)
			pm.setAttr(allObj[i]+".r",getRotate)
			pm.setAttr(allObj[i]+".s",getScale)
	else:
		print "Please Select Target Object......",
	
transferAttribute()