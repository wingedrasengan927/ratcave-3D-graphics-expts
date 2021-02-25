import pyglet
import ratcave as rc
from pyglet.window import key

keys = key.KeyStateHandler()
print(keys)

window = pyglet.window.Window()

window.push_handlers(keys)

# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# get multiple meshes
monkey_smooth = obj_reader.get_mesh("MonkeySmooth", position=(0.5, 0, -1.5), scale=.6)
torus = obj_reader.get_mesh("Torus", position=(-0.5, 0, -1.5), scale=.4)

# create a scene and put the objects in it
scene = rc.Scene(meshes=[monkey_smooth, torus])

# render the scene
@window.event
def on_draw():
    with rc.default_shader:
          scene.draw()

# define a function to rotate the meshes every frame
def rotate_meshes(dt):
    monkey_smooth.rotation.y += 15 * dt  # dt is the time between frames
    torus.rotation.x += 80 * dt

# define a function to move the camera at every frame whenever a keyboard key is pressed
def move_camera(dt):
  camera_speed = 3
  if keys[key.LEFT]:
      scene.camera.position.x -= camera_speed * dt
  if keys[key.RIGHT]:
      scene.camera.position.x += camera_speed * dt


pyglet.clock.schedule(move_camera)
pyglet.clock.schedule(rotate_meshes)


if __name__ == "__main__":
    pyglet.app.run()
