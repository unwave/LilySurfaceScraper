import bpy

# Test regular material
bpy.ops.object.lily_surface_import(
	url="https://cc0textures.com/view?id=Ground023",
	variant="2K-JPG"
)

# Test two-sided
bpy.ops.object.lily_surface_import(
	url="https://www.cgbookcase.com/textures/autumn-leaf-30",
	variant="2K Twosided"
)

# Test World
bpy.ops.object.lily_world_import(
	url="https://hdrihaven.com/hdri/?h=the_lost_city",
	variant="4k"
)

# Test multiple base colors
bpy.ops.object.lily_world_import(
	url="https://texturehaven.com/tex/?t=fabric_pattern_05",
	variant="1k JPG 4 MB"
)
