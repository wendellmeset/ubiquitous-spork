import bpy

def create_pyramid():
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(0,0,0))
    bpy.ops.transform.resize(value=(1, 1, 0.5))
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_extrude={"value":(0, 0, 1)})
    bpy.ops.object.editmode_toggle()

for i in range(5):
    create_pyramid()
    bpy.context.active_object.location.x += 2

