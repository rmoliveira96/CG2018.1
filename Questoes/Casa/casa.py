from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0
dy = 0
dz = 0

# texture = []

def LoadTextures():
    global texture
    texture = glGenTextures(6) #Carregando 6 texturas

   #Textura fundo e esquerda ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='img1.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

   #Textura frente e direita ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[1])
    reader = png.Reader(filename='img2.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

   #Textura do telhado ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[2])
    reader = png.Reader(filename='img3.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

   #Textura do chao     ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[3])
    reader = png.Reader(filename='base.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

   #Textura da porta      ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[4])
    reader = png.Reader(filename='porta.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

   #Textura da porta      ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[5])
    reader = png.Reader(filename='janelaDupla.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1

    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   

    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(0.0,0.0,-5.0)            

    glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    glRotatef(zrot,0.0,0.0,1.0) 
    
    glBindTexture(GL_TEXTURE_2D, texture[1])

    glBegin(GL_QUADS)
    #FRENTE
    glTexCoord2f(0.0,1.0); glVertex3f(-1.0,0.0,1.5)      
    glTexCoord2f(0.0,1.0/2.5); glVertex3f(-1.0,2.0,1.5)   
    glTexCoord2f(1.0/2.0,1.0/2.5); glVertex3f(1.0,2.0,1.5)  
    glTexCoord2f(1.0/2.0,1.0); glVertex3f(1.0,0.0,1.5)  
    glEnd()

    glBegin(GL_TRIANGLES)
    glTexCoord2f(0.0,1.0/2.5); glVertex3f(-1.0,2.0,1.5) 
    glTexCoord2f(1.0/4.0,0.0); glVertex3f(0.0,3.0,1.5)   
    glTexCoord2f(1.0/2.0,1.0/2.45); glVertex3f(1.0,2.0,1.5) 
    glEnd()

    glBegin(GL_QUADS)              
    #DIREITA
    glTexCoord2f(1.0/2.0,1.0); glVertex3f(1.0,0.0,1.5)   
    glTexCoord2f(1.0/2.0,1.0/2.5); glVertex3f(1.0,2.0,1.5)   
    glTexCoord2f(1.0,1.0/2.5); glVertex3f(1.0,2.0,-1.5)  
    glTexCoord2f(1.0,1.0); glVertex3f(1.0,0.0,-1.5)
    glEnd()
    
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)
    #TRAS
    glTexCoord2f(0.0,1.0); glVertex3f(-1.0,0.0,-1.5)      
    glTexCoord2f(0.0,1.0/2.5); glVertex3f(-1.0,2.0,-1.5)     
    glTexCoord2f(1.0/2.0,1.0/2.5); glVertex3f(1.0,2.0,-1.5)  
    glTexCoord2f(1.0/2.0,1.0); glVertex3f(1.0,0.0,-1.5)  
    glEnd()

    glBegin(GL_TRIANGLES)
    glTexCoord2f(0.0,1.0/2.5); glVertex3f(-1.0,2.0,-1.5) 
    glTexCoord2f(1.0/4.0,0.0); glVertex3f(0.0,3.0,-1.5)   
    glTexCoord2f(1.0/2.0,1.0/2.5); glVertex3f(1.0,2.0,-1.5) 
    glEnd()
    
    glBegin(GL_QUADS)              
    #ESQUERDA  
    glTexCoord2f(1.0/2.0,1.0); glVertex3f(-1.0,0.0,1.5)      
    glTexCoord2f(1.0/2.0,1.0/2.5); glVertex3f(-1.0,2.0,1.5)   
    glTexCoord2f(1.0,1.0/2.5); glVertex3f(-1.0,2.0,-1.5)  
    glTexCoord2f(1.0,1.0); glVertex3f(-1.0,0.0,-1.5)  
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[2])
    glBegin(GL_QUAD_STRIP)    
    #TELHADO
    glTexCoord2f(0.0,0.0); glVertex3f(-1.1,1.9,1.6)      
    glTexCoord2f(0.0,1.0); glVertex3f(-1.1,1.9,-1.6)   
    glTexCoord2f(0.5,0.0); glVertex3f(0.0,3.0,1.6)  
    glTexCoord2f(0.5,1.0); glVertex3f(0.0,3.0,-1.6)  
    glTexCoord2f(1.0,0.0); glVertex3f(1.1,1.9,1.6)      
    glTexCoord2f(1.0,1.0); glVertex3f(1.1,1.9,-1.6)   
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[3])
    glBegin(GL_QUAD_STRIP)    
    #CHAO
    glTexCoord2f(0.0,0.0); glVertex3f(-3.0,0.0,-2.3)      
    glTexCoord2f(0.0,1.0); glVertex3f(-3.0,0.0,2.4)   
    glTexCoord2f(1.0,0.0); glVertex3f(1.6,0.0,-2.3)      
    glTexCoord2f(1.0,1.0); glVertex3f(1.6,0.0,2.4)   
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[4])
    glBegin(GL_QUADS)
    #PORTA
    glTexCoord2f(0.0,1.0); glVertex3f(0.24,0.09,1.5001)      
    glTexCoord2f(0.0,0.0); glVertex3f(0.24,1.18,1.5001)   
    glTexCoord2f(1.0,0.0); glVertex3f(0.73,1.18,1.5001)      
    glTexCoord2f(1.0,1.0); glVertex3f(0.73,0.09,1.5001)   
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[5])
    glBegin(GL_QUADS)
    #JANELA GRANDE
    glTexCoord2f(0.0,1.0); glVertex3f(-1.0001,0.42,0.48)      
    glTexCoord2f(0.0,0.0); glVertex3f(-1.0001,1.20,0.48)   
    glTexCoord2f(1.0,0.0); glVertex3f(-1.0001,1.20,-0.6)      
    glTexCoord2f(1.0,1.0); glVertex3f(-1.0001,0.42,-0.6)   
    glEnd()

    glBegin(GL_QUADS)
    #JANELA FRENTE
    glTexCoord2f(0.0,1.0); glVertex3f(-0.69,0.45,1.5001)      
    glTexCoord2f(0.0,0.0); glVertex3f(-0.69,1.20,1.5001)   
    glTexCoord2f(0.5,0.0); glVertex3f(-0.29,1.20,1.5001)      
    glTexCoord2f(0.5,1.0); glVertex3f(-0.29,0.45,1.5001)
    glEnd()

  
    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 0.5
        dy = 0
        dz = 0   
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 0.5
        dz = 0   
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 0.5

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print ("ESQUERDA")
        #xrot -= dx                # X rotation
        yrot -= 5.0                 # Y rotation
        #zrot -= 0.0                     
    elif tecla == GLUT_KEY_RIGHT:
        print ("DIREITA")
       # xrot += dx                # X rotation
        yrot += 5.0                 # Y rotation
       # zrot -= 0.0                     
    elif tecla == GLUT_KEY_UP:
        print ("CIMA")
        xrot -= 5.0                 # X rotation
	#yrot -= 0.0                 
        #zrot += 0.0  
    elif tecla == GLUT_KEY_DOWN:
        print ("BAIXO")
        xrot += 5.0                 # X rotation
	#yrot -= 0.1                 # Y rotation
        #zrot -= dz  

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 1200 x 900 window 
    glutInitWindowSize(1200,900)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Casa")

    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)

    glutSpecialFunc(teclaEspecialPressionada)

    # Initialize our window. 
    InitGL(1200,900)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print ("Hit ESC key to quit.")
    main()
