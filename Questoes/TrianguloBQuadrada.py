from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices = (
    ( 1, 0, 1),
    ( 1, 0,-1),
    (-1, 0, 1),
    (-1, 0,-1),
    ( 0, 1, 0),
    )

linhas = (
    (0,1),
    (0,2),
    (1,3),
    (2,3),
    (0,4),
    (1,4),
    (2,4),
    (3,4),
   )

faces = (
    (0,1,4),
    (0,2,4),
    (2,3,4),
    (1,3,4),
    )

def TrianguloBQuadrada():
    glBegin(GL_QUADS)
    glColor3f(1,0,1)
    glVertex3f(1,0,1)
    glVertex3f(1,0,-1)
    glVertex3f(-1,0,-1)
    glVertex3f(-1,0,1)        
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,0)
    glVertex3f(0,1,0)
    glColor3f(0,1,0)
    glVertex3f(1,0,1)
    glColor3f(0,1,0)
    glVertex3f(1,0,-1)
    glColor3f(0,1,1)
    glVertex3f(-1,0,-1)
    glColor3f(0,0,1)
    glVertex3f(-1,0,1)
    glColor3f(0,1,0)
    glVertex3f(1,0,1)
    glEnd()

    glColor3fv((0,0,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,0,0)
    TrianguloBQuadrada()
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

