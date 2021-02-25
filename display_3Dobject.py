import pyglet
import ratcave as rc

window = pyglet.window.Window()

# loading 3D objects

# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# Check which meshes can be found inside the Wavefront file, and extract it into a Mesh object for rendering.
print(obj_reader.bodies.keys())

# get the monkey object
monkey_smooth = obj_reader.get_mesh("MonkeySmooth")

# get the object's original position
print(monkey_smooth.position)

# change the position of the object
'''
Note: By default, as per OpenGLs convention, the camera is located in the origin 
and points towards the -Z axis. 
Play with the objects coordinates below, and see the camera's viewing frustrum
'''
monkey_smooth.position.xyz = 0, 2, -10

# create a scene and put the monkey object in it
scene = rc.Scene(meshes=[monkey_smooth])
 
@window.event
def on_draw():
    with rc.default_shader:
          scene.draw()

def update(dt):
    '''
    Anything you want done between frames (updating positions, logging events, etc) can go in this function.
    '''
    pass

pyglet.clock.schedule(update)


if __name__ == "__main__":
    pyglet.app.run()
