import bpy  
from mathutils import Vector

# useful shortcut
scene = bpy.context.scene

# when you start default Blender project, first object in scene is a Cube
kostka = scene.objects[0]

# you can change location of object simply by setting the values
kostka.location = (1,2,0)

# same with rotation
kostka.rotation_euler = (0,0,0)

# this will make object cease from current scene
scene.objects.unlink(kostka)

# clear everything for now
scene.camera = None  
for obj in scene.objects:  
    scene.objects.unlink(obj)

# The lab start here...    
######################################################################################################
#First...    
# create plane object with location (0,0,0), dimensions (40,40,0), color (green)

bpy.ops.mesh.primitive_plane_add(location=(0,0,0))  

plane = bpy.context.object  

plane.dimensions=(40,40,0)

# Set a new material to the plane and add a color = (0, 1, 0)

mat = bpy.data.materials.new("mat_Plane") #set new material to variable

plane.data.materials.append(mat) #add the material to the object

bpy.context.object.active_material.diffuse_color = (0, 1, 0) #change color

#######################################################################################################

# create a light object to the scene with location (8, -20, 22) and rotation_euler (0.90, 0, -100)

lamp_data = bpy.data.lamps.new(name="lampa", type='SUN')

lamp_data.sky.use_sky = True

lamp_object = bpy.data.objects.new(name="Lamp_1", object_data=lamp_data,)

scene.objects.link(lamp_object)

lamp_object.location = (8,-20,22)

lamp_object.rotation_euler = (0.90,0,-100)

lamp_object.select = True

scene.objects.active = lamp_object




#######################################################################################################

# Set the camera with parameters: location ( 8, -20, 22 ), rotation euler (0.90, 0, -100) and lens = 10

cam_data = bpy.data.cameras.new(name="cam")

cam_ob = bpy.data.objects.new(name="Camera_1", object_data=cam_data)

scene.objects.link(cam_ob)

cam_ob.location = (8,-20,22)

cam_ob.rotation_euler = (0.90, 0, -100)

cam = bpy.data.cameras[cam_data.name]

cam.lens = 10

#######################################################################################################

# create a set of Spheres - Parameters: size = 1 ,  color yellow

for k in range(0,6):
    for i in range (0,3):
        for j in range (0,3):
            
            x = (i*-3)
            
            y = j*3
            
            z = (k*3)+2
            
            # Create a mesh sphere in the scene
            
            bpy.ops.mesh.primitive_uv_sphere_add(location=(x, y, z), size=1)
            
            bpy.ops.object.shade_smooth()
            
            Sphere_obj = bpy.context.object
            
            mat1 = bpy.data.materials.new(name="MaterialName1") #set new material to variable
            
            Sphere_obj.data.materials.append(mat1) #add the material to the object
            
            bpy.context.object.active_material.diffuse_color = (1,1,0 ) #change color

#######################################################################################################
            
# create a set of Cubes

for k in range(0,6):
    for i in range (0, 3):
        for j in range (0, 3):
            
            x = i*3 + 3
            
            y = j*3
            
            z = (k*3)+2
 
            # Create a mesh cube in the scene
            
            bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
            
            Cube_obj = bpy.context.object
            
            mat2 = bpy.data.materials.new(name="MaterialName2") #set new material to variable
            
            Cube_obj.data.materials.append(mat2) #add the material to the object
            
            bpy.context.object.active_material.diffuse_color = (1,0,1 ) #change color
            

            
########################################################################################################
            
# create a set of Cylinders - Parameters : location=(x, y, z), vertices=32, radius=1.0, depth=2.0
#                                          Color: Red 

for k in range(0,6):
    for i in range (0, 3):
        for j in range (0, 3):
            
            x = i*3 + 3
            
            y = (j*-3)-3
            
            z = (k*3)+2
 
            # Create a mesh cylinder in the scene
            
            bpy.ops.mesh.primitive_cylinder_add(location=(x, y, z), vertices=32, radius=1.0, depth=2.0)
            
            cyl_obj = bpy.context.object
            
            mat3 = bpy.data.materials.new(name="MaterialName3") #set new material to variable
            
            cyl_obj.data.materials.append(mat3) #add the material to the object
            
            bpy.context.object.active_material.diffuse_color = (1,0,0) #change color

            

            



            
#################################################################################################################
            
# create a set of Cones - Parameters: Location (x,y,x), vertices = 32, radius1 = 1 , radius2 = 0 , depth = 3
#                                     Color (0,0,1)

for k in range(0,6):
    for i in range (0,3):
        for j in range (0,3):
            
            x = (i*-3)
            
            y = (j*-3)-3
            
            z = (k*3)+2
            
            # Create a mesh sphere in the scene
            
            bpy.ops.mesh.primitive_cone_add(location = (x,y,z), vertices = 32, radius1 = 1 , radius2 = 0 , depth = 3)
            
            cones_obj = bpy.context.object
            
            mat4 = bpy.data.materials.new(name="MaterialName4") #set new material to variable
            
            cones_obj.data.materials.append(mat4) #add the material to the object
            
            bpy.context.object.active_material.diffuse_color = (0,0,1 ) #change color