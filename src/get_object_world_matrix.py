"""
Get an object world matrix as MMatrix
"""

import maya.api.OpenMaya as OpenMaya

# create a cube
cube = cmds.polyCube()[0]
cmds.xform(cube, t=[1,2,3], ro=[10,15,32], ws=1)

# OpenMaya way ----------------------------

# get a dag path of the cube
selection_list = om.MSelectionList()
selection_list.add(cube)
dag_path = selection_list.getDagPath(0)

# get world matrix
world_matrix = dag_path.inclusiveMatrix() # gives us pCube1 world matrix


# maya cmds way ---------------------------

import maya.cmds as cmds
world_matrix = cmds.xform('pCube1', q=True, worldSpace=True, matrix=True)
