import pyglet
import ratcave as rc
from pyglet.window import key

# defining a window and configuring it to use keys
keys = key.KeyStateHandler()
window = pyglet.window.Window(resizable=True)
window.push_handlers(keys)

model_file = rc.resources.obj_primitives
monkey_smooth = rc.WavefrontReader(model_file).get_mesh('MonkeySmooth')

# since our camera is going to be located at the origin (Initially)
# we place the object at a depth of 2.5 from the camera
monkey_smooth.position.xyz = 0, 0, -2.5

# Note: You can also scale along X, Y, Z directions separately
monkey_smooth.scale = 0.4

# there are some parameters that the OrthoProjection is going to take,
# But I couldn't figure out what their significance is (especially coords="absolute" wala one),  
# and I guess it doesn't really matter
projection = rc.OrthoProjection()
# Put projection=None to get back to normal projection
# switch between normal projection and orthographic projection
# and observe the difference between them
camera = rc.Camera(projection=projection)

# create a scene and put the objects in it, and use our custom camera
scene = rc.Scene(meshes=[monkey_smooth], camera=camera)

# render the scene
@window.event
def on_draw():
    window.clear()
    with rc.default_shader, rc.default_states, camera:
        scene.draw()

# define a function to move the camera at every frame whenever a keyboard key is pressed
def move_camera(dt):
    # we look at the object no matter where we place the camera
    # comment this and observe the difference
    camera.look_at(0, 0, -2.5)

    camera_speed = 3
    if keys[key.LEFT]:
        camera.position.x -= camera_speed * dt
    if keys[key.RIGHT]:
        camera.position.x += camera_speed * dt
    if keys[key.UP]:
        camera.position.y += camera_speed * dt
    if keys[key.DOWN]:
        camera.position.y -= camera_speed * dt
    if keys[key.W]:
        camera.position.z += camera_speed * dt
    if keys[key.S]:
        camera.position.z -= camera_speed * dt


pyglet.clock.schedule(move_camera)

if __name__ == "__main__":
    pyglet.app.run()