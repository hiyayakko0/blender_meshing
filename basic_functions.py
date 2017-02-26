import bpy
import object_printed3d_utils

f = open('report.txt', '

#objのself_intersect_facesを書き出し
obj = bpy.data.objects[0]
len(object_print3d_utils.mesh_helpers.bmesh_check_self_intersect_object(obj))
