# Ratcave 3D Graphics Notes, Experiments and Tutorials

Repo containing different experiments and my observations with ratcave with majority of tutorials taken from the official repo.

## General Observations

* The projection matrix remains constant for a camera (to confirm)

## Orthographic projection

* In orthographic projection, the light rays come from infinity in the direction the camera is looking at, and project an Image of the object on a plane perpendicular to the direction of light.
* Because the light rays come from Infinity, we cannot estimate how far the object is from the camera; There is no notion of depth in orthographic projection.
* You can test this out by running the demo `orthographic_projection.py` and comparing the image from both the projections.
* Also, in Orthographic projection, it's better  to manipulate the object itself (rotate and scale) rather than moving the camera.
* For more notes you can check the `orthographic_projection.py` file.