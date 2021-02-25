import pyglet
import ratcave as rc
from pyglet.window import key

keys = key.KeyStateHandler()

window = pyglet.window.Window(resizable=True)

window.push_handlers(keys)

model_file = rc.resources.obj_primitives
monkey_smooth = rc.WavefrontReader(model_file).get_mesh('MonkeySmooth')
monkey_smooth.position.xyz = 0, 0, -2.5
monkey_smooth.scale = 0.4

projection = rc.OrthoProjection()
camera = rc.Camera(projection=projection)

# create a scene and put the objects in it
scene = rc.Scene(meshes=[monkey_smooth], camera=camera)

@window.event
def on_draw():
    window.clear()
    with rc.default_shader, rc.default_states, camera:
        scene.draw()

# define a function to move the camera at every frame whenever a keyboard key is pressed
def move_camera(dt):
    camera.look_at(0, 0, -2.5)
    camera_speed = 3
    print(camera.uniforms['projection_matrix'])
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