........Facial Rig ......


'''
Lip Setup
Create Lips Locator
'''

import pymel.core as pm
def lip_setup():
	LipUpper_M = pm.spaceLocator(n="LipUpper_M",p=[0,1,0])
	LipUpper_L = pm.spaceLocator(n="LipUpper_L",p=[1,.5,0])
	LipLower_L = pm.spaceLocator(n="LipLower_L",p=[1,-.5,0])
	Lip_L = pm.spaceLocator(n="Lip_L",p=[2,0,0])
	LipLower_M = pm.spaceLocator(n="LipLower_M",p=[0,-1,0])
	LipLower_R = pm.spaceLocator(n="LipLower_R",p=[-1,-.5,0])
	LipUpper_R = pm.spaceLocator(n="LipUpper_R",p=[-1,.5,0])
	Lip_R = pm.spaceLocator(n="Lip_R",p=[-2,0,0])
	lipLoc = pm.select(LipUpper_M,LipUpper_L,LipLower_L,Lip_L,LipLower_M,LipLower_R,LipUpper_R,Lip_R)
	lipGrp = pm.group(n = "lipGrp")
	lipPivot = pm.listRelatives(lipGrp,c=True)
	pm.xform(lipPivot,cp=True)
	print ("LipSetup Created Please set the Locator Position"),

lip_setup()



'''
Create Joint on Lips Locator
'''

import pymel.core as pm
def LipsBuild():
	pm.select(cl=True)
	lipLocs = pm.listRelatives("lipGrp",c=True)
	lipJntGrp = pm.group(n = "LipJnt_Grp")
	for i in range(len(lipLocs)):
		pm.select(cl=True)
		jntName = lipLocs[i].split("_")
		lipJnt = pm.joint(n=jntName[0]+"Jnt_"+jntName[1])
		pm.delete(pm.parentConstraint(lipLocs[i],lipJnt))
		pm.parent(lipJnt,lipJntGrp)

	### Lips Ctrl Created on Locators ###
	lipJntHier = pm.listRelatives(lipJntGrp,c=True)
	pm.select(cl=True)
	lipCtrlGrp = pm.group(n="LipCtrl_Grp")
	for i in range(len(lipJntHier)):
		pm.select(cl=True)
		jntCtrlName = lipJntHier[i].split("Jnt")
		offsetJnt = pm.joint(n="FKOffset"+jntCtrlName[0]+jntCtrlName[1])
		pm.setAttr(offsetJnt+".drawStyle",2)
		pm.select(cl=True)
		extraGrp = pm.group(n="FKExtra"+jntCtrlName[0]+jntCtrlName[1])
		pm.parent(extraGrp,offsetJnt)
		pm.select(cl=True)
		ctrl = pm.circle(n="FK"+jntCtrlName[0]+jntCtrlName[1]+"_CTRL",r=.2,ch=False)
		fkxJnt = pm.joint(n="FKX"+jntCtrlName[0]+jntCtrlName[1])
		pm.setAttr(fkxJnt+".drawStyle",2)
		pm.parent(ctrl[0],extraGrp)
		pm.parent(offsetJnt,lipCtrlGrp)
		pm.delete(pm.parentConstraint(lipJntHier[i],offsetJnt))
		pm.parentConstraint(fkxJnt,lipJntHier[i])
	pm.select(cl=True)
	lipGrp = pm.group(n = "LipGrp")
	pm.parent([lipCtrlGrp,lipJntGrp],lipGrp)
	pm.select(cl=True)
	if not pm.objExists("FacialGroup"):
		facialgrp = pm.group(n = "FacialGroup")
	pm.parent(lipGrp,"FacialGroup")
	
	pm.delete("lipGrp")
	pm.select(cl=True)
	### Lip Mover......
	lipmoverGrp = pm.group(n="LipMoverGrp")
	lipmoverCtrl = pm.circle(n="LipMover_CTRL",ch=False)
	pm.parent(lipmoverCtrl,lipmoverGrp)
	pm.delete(pm.parentConstraint("LipGrp",lipmoverGrp))
	pm.xform("LipMoverGrp",t=[0,0,1])
	pm.parentConstraint(lipmoverCtrl,"LipGrp",mo=True)
	pm.parent(lipmoverGrp,"FacialGroup")
	
	
	print ("Lips Build......."),

LipsBuild()


'''
.............................................................................................................................................................
'''



'''
EyeBrow Setup
Create EyeBrows Locator
'''

import pymel.core as pm
def eyeBrow_setup():
	EyeBrowInner_L = pm.spaceLocator(n="EyeBrowInner_L",p=[2,6,0])
	EyeBrowMid_L = pm.spaceLocator(n="EyeBrowMid_L",p=[3.2,6.2,0])
	EyeBrowOuter_L = pm.spaceLocator(n="EyeBrowOuter_L",p=[4.4,6,0])
	EyeBrowInner_R = pm.spaceLocator(n="EyeBrowInner_R",p=[-2,6,0])
	EyeBrowMid_R = pm.spaceLocator(n="EyeBrowMid_R",p=[-3.2,6.2,0])
	EyeBrowOuter_R = pm.spaceLocator(n="EyeBrowOuter_R",p=[-4.4,6,0])
	eyeBrowLoc = pm.select(EyeBrowInner_L,EyeBrowMid_L,EyeBrowOuter_L,EyeBrowInner_R,EyeBrowMid_R,EyeBrowOuter_R)
	eyeBrowGrp = pm.group(n = "eyeBrowGrp")
	eyeBrowPivot = pm.listRelatives(eyeBrowGrp,c=True)
	pm.xform(eyeBrowPivot,cp=True)	
	grp = pm.group(n = "EyeBrowSetup")
	print ("EyeBrowSetup Created Please set the Locator Position"),
eyeBrow_setup()


'''
Create Joint on EyeBrow Locator
'''

import pymel.core as pm
def eyeBrowBuild():
	pm.select(cl=True)
	eyeBrowLocs = pm.listRelatives("eyeBrowGrp",c=True)
	eyeBrowJntGrp = pm.group(n = "EyeBrowJnt_Grp")
	for i in range(len(eyeBrowLocs)):
		pm.select(cl=True)
		jntName = eyeBrowLocs[i].split("_")
		eyeBrowJnt = pm.joint(n=jntName[0]+"Jnt_"+jntName[1])
		pm.delete(pm.parentConstraint(eyeBrowLocs[i],eyeBrowJnt))
		pm.parent(eyeBrowJnt,eyeBrowJntGrp)

	### EyeBrow Ctrl Created on Locators ###
	pm.select(cl=True)
	eyeBrowGrpHier =  pm.listRelatives(eyeBrowJntGrp,c=True)
	pm.select(cl=True)
	eyeBrowCtrlGrp = pm.group(n="EyeBrowCtrl_Grp")
	for y in range(len(eyeBrowGrpHier)):
		pm.select(cl=True)
		eyeBrowCtrlName = eyeBrowGrpHier[y].split("Jnt")
		eyeBrowOffsetJnt = pm.joint(n="FKOffset"+eyeBrowCtrlName[0]+eyeBrowCtrlName[1])
		pm.setAttr(eyeBrowOffsetJnt+".drawStyle",2)
		pm.select(cl=True)
		EyeBrowExtraGrp = pm.group(n="FKExtra"+eyeBrowCtrlName[0]+eyeBrowCtrlName[1])
		pm.parent(EyeBrowExtraGrp,eyeBrowOffsetJnt)
		pm.select(cl=True)
		eyeBrowCtrl = pm.circle(n="FK"+eyeBrowCtrlName[0]+eyeBrowCtrlName[1]+"_CTRL",r=.2,ch=False)
		eyeBrowFkxJnt = pm.joint(n="FKX"+eyeBrowCtrlName[0]+eyeBrowCtrlName[1])
		pm.setAttr(eyeBrowFkxJnt+".drawStyle",2)
		pm.parent(eyeBrowCtrl[0],EyeBrowExtraGrp)
		pm.parent(eyeBrowOffsetJnt,eyeBrowCtrlGrp)
		pm.delete(pm.parentConstraint(eyeBrowGrpHier[y],eyeBrowOffsetJnt))
		pm.parentConstraint(eyeBrowFkxJnt,eyeBrowGrpHier[y])

	pm.select(cl=True)
	eyeBrowGrp = pm.group(n="EyeBrowGrp")
	pm.parent([eyeBrowCtrlGrp,eyeBrowJntGrp],eyeBrowGrp)
	pm.select(cl=True)
	if not pm.objExists("FacialGroup"):
		facialgrp = pm.group(n = "FacialGroup")
	pm.parent(eyeBrowGrp,"FacialGroup")
	
	pm.delete("EyeBrowSetup")
	
	print ("EyeBrow Build......."),

eyeBrowBuild()



#.......................................................................................................................................................


'''
Locator create for Nose Sneer and Muzzle.
'''
import pymel.core as pm
def nose_setup():
	l_noseLoc = pm.spaceLocator(n="SneerLoc_L",p=[0.5,3,0])
	r_noseLoc = pm.spaceLocator(n="SneerLoc_R",p=[-0.5,3,0])
	muzzleLoc = pm.spaceLocator(n="MuzzleLoc",p=[0,5.5,0])
	noseGrp = pm.group(n="NoseSetup")
	pm.parent([l_noseLoc,r_noseLoc],noseGrp)
	noseGrpHier = pm.listRelatives(noseGrp,c=True)
	for i in range(len(noseGrpHier)):
		pm.xform(noseGrpHier[i]	,cp=True)
		
	pm.select(cl=True)
		
nose_setup()




'''
Create Nose joint on Locator.
'''

import pymel.core as pm
def NoseBuild():
	noseLocHier = pm.listRelatives("NoseSetup",c=True)
	NosejntGrp = pm.group(n="NoseJnt_Grp")
	for i in range(len(noseLocHier)):
		name = noseLocHier[i].split("Loc")
		jnt = pm.joint(n=name[0]+"Jnt"+name[1])
		pm.delete(pm.parentConstraint(noseLocHier[i],jnt))
		pm.parent(jnt,jntGrp)
		pm.select(cl=True)
		
	### Nose Ctrl Created on Joints ###
	noseJntGrpHier = pm.listRelatives(NosejntGrp,c=True)
	pm.select(cl=True)
	noseCtrlGrp = pm.group(n="NoseCtrl_Grp")
	for i in range(len(noseJntGrpHier)):
		pm.select(cl=True)
		jntCtrlName = noseJntGrpHier[i].split("Jnt")
		offsetJnt = pm.joint(n="FKOffset"+jntCtrlName[0]+jntCtrlName[1])
		pm.setAttr(offsetJnt+".drawStyle",2)
		pm.select(cl=True)
		extraGrp = pm.group(n="FKExtra"+jntCtrlName[0]+jntCtrlName[1])
		pm.parent(extraGrp,offsetJnt)
		pm.select(cl=True)
		ctrl = pm.circle(n="FK"+jntCtrlName[0]+jntCtrlName[1]+"_CTRL",r=.2,ch=False)
		fkxJnt = pm.joint(n="FKX"+jntCtrlName[0]+jntCtrlName[1])
		pm.setAttr(fkxJnt+".drawStyle",2)
		pm.parent(ctrl[0],extraGrp)
		pm.parent(offsetJnt,noseCtrlGrp)
		pm.delete(pm.parentConstraint(noseJntGrpHier[i],offsetJnt))
		pm.parentConstraint(fkxJnt,noseJntGrpHier[i])
	
	pm.parent(["FKOffsetSneer_L","FKOffsetSneer_R"],"FKXMuzzle")
	pm.select(cl=True)
	noseGrp = pm.group(n="NoseGrp")
	pm.parent([NosejntGrp,noseCtrlGrp],noseGrp)
	pm.delete("NoseSetup")
	
	if not pm.objExists("FacialGroup"):
		pm.group(n="FacialGroup")
	pm.parent(noseGrp,"FacialGroup")
	
	print ("Sneer Build"),

NoseBuild()