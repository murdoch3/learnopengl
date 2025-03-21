import pygame
import OpenGL

from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 

# The 8 vertices of the cube
vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# The 12 edges between the vertices of the cube
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

def Cube():
    glBegin(GL_LINES)
    # For each edge of the cube
    for edge in edges:
        # For each vertex in the edge
        for vertex in edge:
            # We'll "send" the vertex to OpenGL
            # Since it knows we're drawing lines (GL_LINES), it will draw a line
            # appropriately between the two points
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    # Use pygame to create an opengl window
    pygame.init() 
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Set our perspective
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Move view matrix back 5 units so we can see the cube
    glTranslatef(0.0, 0.0, -5.0)

    # Event loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw
        #   Multiplies current matrix by the rotation matrix
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()