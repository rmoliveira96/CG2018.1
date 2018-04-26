from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def PrismaBQuadrada():
    #BAIXO
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex3f(-0.5,0,0.5)
    glVertex3f(0.5,0,0.5)
    glVertex3f(0.5,0,-0.5)
    glVertex3f(-0.5,0,-0.5)     
    glEnd()

    #CIMA
    glBegin(GL_QUADS)
    glColor3f(0,0,1)
    glVertex3f(-0.5,2.0,0.5)
    glVertex3f(0.5,2.0,0.5)
    glVertex3f(0.5,2.0,-0.5)
    glVertex3f(-0.5,2.0,-0.5)        
    glEnd()

    #LADOS
    glBegin(GL_QUAD_STRIP)
    glColor3f(0,1,1)
    glVertex3f(0.5,2.0,-0.5)
    glVertex3f(0.5,0.0,-0.5)
    glVertex3f(-0.5,2.0,-0.5)
    glVertex3f(-0.5,0.0,-0.5)
    glVertex3f(-0.5,2.0,0.5)
    glVertex3f(-0.5,0.0,0.5)
    glVertex3f(0.5,2.0,0.5)
    glVertex3f(0.5,0.0,0.5)
    glVertex3f(0.5,2.0,-0.5)
    glVertex3f(0.5,0.0,-0.5)
    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,0.5,0)
    PrismaBQuadrada()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc((1000/60),timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()

