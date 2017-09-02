import pymel.core as pm

###............FK To IK Prepare Switch.................###

###Create Group for foot Switch###

def prepare_rig_FkToIk():
	selection = pm.ls(sl=True)
	if len(selection)>0:
		side = selection[0].split('_')[1]
		ikFootCtrl = 'IKLeg_'+side+'_CTRL'
		fkAnkleCtrl = 'FKAnkle_'+side+'_CTRL'
		poleLeg = 'PoleLeg_'+side+'_CTRL'
		fkKneeCtrl = 'FKKnee_'+side+'_CTRL'
		FootdummyCtrl = 'legSwitch_'+side+'_CTRL'
		FootdummyGrp = 'legSwitch_'+side+'_Grp'
		KneedummyCtrl = 'kneeSwitch_'+side+'_CTRL'
		KneedummyGrp = 'kneeSwitch_'+side+'_Grp'
		
		
		if not pm.objExists(FootdummyGrp):
			FootdummyCtrl = pm.group(n=FootdummyCtrl,em=True)
			FootdummyGrp = pm.group(n=FootdummyGrp)
			pm.delete(pm.parentConstraint(ikFootCtrl,FootdummyGrp))
			pm.parent(FootdummyGrp,fkAnkleCtrl)
			
		if not pm.objExists(KneedummyGrp):
			KneedummyCtrl = pm.group(n=KneedummyCtrl,em=True)
			KneedummyGrp = pm.group(n=KneedummyGrp)
			pm.delete(pm.parentConstraint(poleLeg,KneedummyGrp))
			pm.parent(KneedummyGrp,fkKneeCtrl)
	else:
		print 'please select controller',

prepare_rig_FkToIk()
	
	


#.........................................................................................#


#this is for riggers. it creates groups to help in orientation
import pymel.core as pm


def prepare_rig_IkToFK():
	selection = pm.ls(sl=True)
	if len(selection)>0:
		side = selection[0].split('_')[1]
		hipSwitchCtrl = 'FK_hip_switch_'+side+'_Ctrl'
		hipSwitchGrp = 'FK_hip_switch_'+side+'_Grp'
		hipJnt = 'Hip_'+side
		kneeSwitchCtrl = 'FK_knee_switch_'+side+'_Ctrl'
		kneeSwitchGrp = 'FK_knee_switch_'+side+'_Grp'
		kneeJnt = 'Knee_'+side
		ankleSwitchCtrl = 'FK_ankle_switch_'+side+'_Ctrl'
		ankleSwitchGrp = 'FK_ankle_switch_'+side+'_Grp'
		ankleJnt = 'Ankle_'+side
		
		
		
		if not pm.objExists(hipSwitchGrp):
			hipSwitchCtrl = pm.group(n=hipSwitchCtrl,em=True)
			hipSwitchGrp = pm.group(n=hipSwitchGrp)
			pm.delete(pm.parentConstraint(hipJnt,hipSwitchGrp))
			pm.parent(hipSwitchGrp,hipJnt)
		
		if not pm.objExists(kneeSwitchGrp):
			kneeSwitchCtrl = pm.group(n=kneeSwitchCtrl,em=True)
			kneeSwitchGrp = pm.group(n=kneeSwitchGrp)
			pm.delete(pm.parentConstraint(kneeJnt,kneeSwitchGrp))
			pm.parent(kneeSwitchGrp,kneeJnt)
		
		if not pm.objExists(ankleSwitchGrp):
			ankleSwitchCtrl = pm.group(n=ankleSwitchCtrl,em=True)
			ankleSwitchGrp = pm.group(n=ankleSwitchGrp)
			pm.delete(pm.parentConstraint(ankleJnt,ankleSwitchGrp))
			pm.parent(ankleSwitchGrp,ankleJnt)
	else:
		print 'please select controller',
	
	
prepare_rig_IkToFK()

##.............................................................................................................................##

import pymel.core as pm

###Switch between FK To IK Leg###
def Fk_To_Ik_Switch_Button():
	selection = pm.ls(sl=True)
	namespace_correct = selection[0].split(':')[:-1]
	if len(selection)>0:
		side = selection[0].split('_')[1]
		locFoot = namespace_correct[0]+':'+'tempFootLOC'
		FootdummyCtrl = namespace_correct[0]+':'+'legSwitch_'+side+'_CTRL'
		ikFootCtrl = namespace_correct[0]+':'+'IKLeg_'+side+'_CTRL'
		locKnee = namespace_correct[0]+':'+'tempKneeLOC'
		KneedummyCtrl = namespace_correct[0]+':'+'kneeSwitch_'+side+'_CTRL'
		poleLeg = namespace_correct[0]+':'+'PoleLeg_'+side+'_CTRL'
		
		
		
		
		locFoot = pm.spaceLocator(n=locFoot)
		snaploc = pm.delete(pm.parentConstraint(FootdummyCtrl,locFoot))
		pm.delete(pm.parentConstraint(locFoot,ikFootCtrl,mo=False),locFoot)
		
		###Switch between FK To IK Leg###
		
		locKnee = pm.spaceLocator(n=locKnee)
		snaploc = pm.delete(pm.parentConstraint(KneedummyCtrl,locKnee))
		pm.delete(pm.pointConstraint(locKnee,poleLeg,mo=False),locKnee)
		
		pm.setAttr(selection[0]+'.FKIKBlend',10)
	else:
		print 'select switch controller',

Fk_To_Ik_Switch_Button()
	
	
'''
selection = pm.ls(sl=True)
namespace_var = selection[0].split(':')[:-1]
pm.select(namespace_var[0] + ':' + 'Placement_CTRL')
'''


###Switch between FK To IK Leg###

def Ik_To_Fk_Switch_Button():
	selection = pm.ls(sl=True)
	namespace_correct = selection[0].split(':')[:-1]
	if len(selection)>0:
		side = selection[0].split('_')[1]
		hipSwitchCtrl = namespace_correct[0]+':'+'FK_hip_switch_'+side+'_Ctrl'
		kneeSwitchCtrl = namespace_correct[0]+':'+'FK_knee_switch_'+side+'_Ctrl'
		ankleSwitchCtrl = namespace_correct[0]+':'+'FK_ankle_switch_'+side+'_Ctrl'
		FKHip_CTRL = namespace_correct[0]+':'+'FKHip_'+side+'_CTRL'
		temp_loc = namespace_correct[0]+':'+'temp_loc'
		switch_ctrl = namespace_correct[0]+':'+'FKIKLeg_'+side+'_CTRL'
		FKKnee_CTRL = namespace_correct[0]+':'+'FKKnee_'+side+'_CTRL'
		FKAnkle_CTRL = namespace_correct[0]+':'+'FKAnkle_'+side+'_CTRL'
		
		
		temp_loc = pm.spaceLocator(n=temp_loc)
		pm.delete(pm.parentConstraint(hipSwitchCtrl,temp_loc))
		pm.delete(pm.parentConstraint(temp_loc,FKHip_CTRL),temp_loc)
		
		
		temp_loc = pm.spaceLocator(n=temp_loc)
		pm.delete(pm.parentConstraint(kneeSwitchCtrl,temp_loc))
		pm.delete(pm.parentConstraint(temp_loc,FKKnee_CTRL),temp_loc)
		
		
		temp_loc = pm.spaceLocator(n=temp_loc)
		pm.delete(pm.parentConstraint(ankleSwitchCtrl,temp_loc))
		pm.delete(pm.parentConstraint(temp_loc,FKAnkle_CTRL),temp_loc)
		
		pm.setAttr(switch_ctrl+'.FKIKBlend',0)		
	else:
		print 'select switch controller',
	
Ik_To_Fk_Switch_Button()
	

	



