import bpy

def convert_to_blender(s):
    side = None
    if "_l_" in s:
        side = "left"
    elif "_r_" in s:
        side = "right"
    
    if side is not None:
        return s.replace("_l_", "_DEFAULT_").replace("_r_", "_DEFAULT_") + "." + side
    else:
        return s

def convert_to_pdx(s):
    side = None
    if ".left" in s:
        side = "l"
    elif ".right" in s:
        side = "r"
    
    if side is not None:
        return s.replace(".left", "").replace(".right", "").replace("_DEFAULT_", "_" + side + "_")
    else:
        return s

def invert(s):
    if "_DEFAULT_" in s:
        return convert_to_pdx(s)
    else:
        return convert_to_blender(s)

for rig in bpy.context.selected_objects:
    if rig.type == 'ARMATURE':
        for mesh in rig.children:
            for vg in mesh.vertex_groups:
                vg.name = invert(vg.name)
        for bone in rig.pose.bones:
            bone.name = invert(bone.name)
    else:
        raise Exception("wrong object selected")