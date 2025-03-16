import pygame
import OpenGL

from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 

def main():
    # Use pygame to create an opengl window
    pygame.init() 
    display = (800, 600)
    pygame.display.set_caption("LearnOpenGL")
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Set our perspective
    #gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Move view matrix back 5 units so we can see the cube
    #glTranslatef(0.0, 0.0, -5.0)

    # Event loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        pygame.display.flip()
        pygame.time.wait(10)

main()