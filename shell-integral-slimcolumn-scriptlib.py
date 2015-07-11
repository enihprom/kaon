def print_shell_selected():
    for i in range(len(bpy.data.objects[2].data.vertices)):
        if bpy.data.objects[2].data.vertices[i].select:
            print(str(bpy.data.objects[2].data.vertices[i].co[0]) + ", " + str(bpy.data.objects[2].data.vertices[i].co[1]) + ", " + str(bpy.data.objects[2].data.vertices.co[2]))