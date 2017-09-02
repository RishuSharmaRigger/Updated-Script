### arm switch ###
### Create Groups for Fk to Ik Arm switch ###
# This script for Riggers Please Run before Rig Published #

import pymel.core as pm

def prepare_rig_FkToIk():
	selection = pm.ls(sl=True)
	if len(selection)>0:
		side = selection[0].split('_')[1]
		ikArmCtrl = 'IKArm_'+side+'_CTRL'
		fkWristCtrl = 'FKWrist_'+side+'_CTRL'
		poleArm = 'PoleArm_'+side+'_CTRL'
		fkElbowCtrl = 'FKElbow_'+side+'_CTRL'
		ArmdummyCtrl = 'ArmSwitch_'+side+'_CTRL'
		ArmdummyGrp = 'ArmSwitch_'+side+'_Grp'
		ElbowdummyCtrl = 'ElbowSwitch_'+side+'_CTRL'
		ElbowdummyGrp = 'ElbowSwitch_'+side+'_Grp'
		
		
		if not pm.objExists(ArmdummyGrp):
			ArmdummyCtrl = pm.group(n=ArmdummyCtrl,em=True)
			ArmdummyGrp = pm.group(n=ArmdummyGrp)
			pm.delete(pm.parentConstraint(ikArmCtrl,ArmdummyGrp))
			pm.parent(ArmdummyGrp,fkWristCtrl)
			
		if not pm.objExists(ElbowdummyGrp):
			ElbowdummyCtrl = pm.group(n=ElbowdummyCtrl,em=True)
			ElbowdummyGrp = pm.group(n=ElbowdummyGrp)
			pm.delete(pm.parentConstraint(poleArm,ElbowdummyGrp))
			pm.parent(ElbowdummyGrp,fkElbowCtrl)
	else:
		print 'please select controller',
	
	
prepare_rig_FkToIk()

............................................................................................................


###............IK To FK Prepare Switch.................###

###Create Group for Arm Switch###
import pymel.core as pm


def prepare_rig_IkToFK():
	selection = pm.ls(sl=True)
	if len(selection)>0:
		side = selection[0].split('_')[1]
		shoulderSwitchCtrl = 'FK_shoulder_switch_'+side+'_Ctrl'
		shoulderSwitchGrp = 'FK_shoulder_switch_'+side+'_Grp'
		shoulderJnt = 'Shoulder_'+side
		ElbowSwitchCtrl = 'FK_Elbow_switch_'+side+'_Ctrl'
		ElbowSwitchGrp = 'FK_Elbow_switch_'+side+'_Grp'
		ElbowJnt = 'Elbow_'+side
		wristSwitchCtrl = 'FK_wrist_switch_'+side+'_Ctrl'
		wristSwitchGrp = 'FK_wrist_switch_'+side+'_Grp'
		wristJnt = 'Wrist_'+side
		
		
		
		if not pm.objExists(shoulderSwitchGrp):
			shoulderSwitchCtrl = pm.group(n=shoulderSwitchCtrl,em=True)
			shoulderSwitchGrp = pm.group(n=shoulderSwitchGrp)
			pm.delete(pm.parentConstraint(shoulderJnt,shoulderSwitchGrp))
			pm.parent(shoulderSwitchGrp,shoulderJnt)
		
		if not pm.objExists(ElbowSwitchGrp):
			ElbowSwitchCtrl = pm.group(n=ElbowSwitchCtrl,em=True)
			ElbowSwitchGrp = pm.group(n=ElbowSwitchGrp)
			pm.delete(pm.parentConstraint(ElbowJnt,ElbowSwitchGrp))
			pm.parent(ElbowSwitchGrp,ElbowJnt)
		
		if not pm.objExists(wristSwitchGrp):
			wristSwitchCtrl = pm.group(n=wristSwitchCtrl,em=True)
			wristSwitchGrp = pm.group(n=wristSwitchGrp)
			pm.delete(pm.parentConstraint(wristJnt,wristSwitchGrp))
			pm.parent(wristSwitchGrp,wristJnt)
	else:
		print 'please select controller',
	
	
prepare_rig_IkToFK()

..................................................................................

##Scripts for animators##
###Switch between FK To IK Arm###

import pymel.core as pm

def Fk_To_Ik_Switch_Button():
	selection = pm.ls(sl=True)
	namespace_correct = selection[0].split(':')[:-1]
	if len(selection)>0:
		side = selection[0].split('_')[1]
		locArm = namespace_correct[0]+':'+'tempArmLOC'
		ArmdummyCtrl = namespace_correct[0]+':'+'ArmSwitch_'+side+'_CTRL'
		ikArmCtrl = namespace_correct[0]+':'+'IKArm_'+side+'_CTRL'
		locElbow = namespace_correct[0]+':'+'tempElbowLOC'
		ElbowdummyCtrl = namespace_correct[0]+':'+'ElbowSwitch_'+side+'_CTRL'
		poleArm = namespace_correct[0]+':'+'PoleArm_'+side+'_CTRL'
		
		
		
		
		locArm = pm.spaceLocator(n=locArm)
		snaploc = pm.delete(pm.parentConstraint(ArmdummyCtrl,locArm))
		pm.delete(pm.parentConstraint(locArm,ikArmCtrl,mo=False),locArm)
		
		###Switch between FK To IK Leg###
		
		locElbow = pm.spaceLocator(n=locElbow)
		snaploc = pm.delete(pm.parentConstraint(ElbowdummyCtrl,locElbow))
		pm.delete(pm.pointConstraint(locElbow,poleArm,mo=False),locElbow)
		
		pm.setAttr(selection[0]+'.FKIKBlend',10)
		
	else:
		print 'select switch controller',
	
	
Fk_To_Ik_Switch_Button()


................................................................................................

###Switch between IK To FK Arm###

import pymel.core as pm

def Ik_To_Fk_Switch_Button():
	selection = pm.ls(sl=True)
	namespace_correct = selection[0].split(':')[:-1]
	if len(selection)>0:
		side = selection[0].split('_')[1]
		shoulderSwitchCtrl = namespace_correct[0]+':'+'FK_shoulder_switch_'+side+'_Ctrl'
		ElbowSwitchCtrl = namespace_correct[0]+':'+'FK_Elbow_switch_'+side+'_Ctrl'
		wristSwitchCtrl = namespace_correct[0]+':'+'FK_wrist_switch_'+side+'_Ctrl'
		FKShoulder_CTRL = namespace_correct[0]+':'+'FKShoulder_'+side+'_CTRL'
		temp_loc = namespace_correct[0]+':'+'temp_loc'
		switch_ctrl = namespace_correct[0]+':'+'FKIKArm_'+side+'_CTRL'
		FKElbow_CTRL = namespace_correct[0]+':'+'FKElbow_'+side+'_CTRL'
		FKWrist_CTRL = namespace_correct[0]+':'+'FKWrist_'+side+'_CTRL'
		
		
		temp_loc = pm.spaceLocator(n=temp_loc)
		pm.delete(pm.parentConstraint(shoulderSwitchCtrl,temp_loc))
		pm.delete(pm.parentConstraint(temp_loc,FKShoulder_CTRL),temp_loc)
		
		
		temp_loc = pm.spaceLocator(n=temp_loc)
		pm.delete(pm.parentConstraint(ElbowSwitchCtrl,temp_loc))
		pm.delete(pm.parentConstraint(temp_loc,FKElbow_CTRL),temp_loc)
		
		
		temp_loc = pm.spaceLocator(n=temp_loc)
		pm.delete(pm.parentConstraint(wristSwitchCtrl,temp_loc))
		pm.delete(pm.parentConstraint(temp_loc,FKWrist_CTRL),temp_loc)
		
		pm.setAttr(switch_ctrl+'.FKIKBlend',0)	
			
	else:
		print 'select switch controller',
	
	
		
Ik_To_Fk_Switch_Button()