#Script for Suffix/Prefix, Search/Replace and Rename
import pymel.core as pm
# suffixName
def suffixName():
	suffixName = ""
	obj = pm.ls(sl=True)
	for i in range(len(obj)):
		rname = pm.rename(obj[i],obj[i]+suffixName)
		
suffixName()
		
# prefixName
def prefixName():
	prefixName = ""
	obj = pm.ls(sl=True)
	for i in range(len(obj)):
		rname = pm.rename(obj[i],prefixName+obj[i])
		
prefixName()	


# search and replace name 
def search_replace():
	search = ""
	replace = ""
	obj = pm.ls("*" + search + "*")
	for i in range(len(obj)):
		renam = pm.rename(obj[i],obj[i].replace(search, replace))
		
search_replace()


# rename 
name = "A"
start = "0"
obj = pm.ls(sl=True)
for i in range(len(obj)):
	renam = pm.rename(obj[i],name+start)