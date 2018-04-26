from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

def PiramideBaseN(n,r):
    #LATERAIS
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,1)
    posicao = piramide(n,r)    
    for i in range(n+1):
        glVertex3fv(posicao[0][i])
    glEnd()

    #BASE
    glBegin(GL_POLYGON)
    glColor3f(0,1,1)
    posicao = piramide(n,r)    
    for i in range(n):
        glVertex3fv(posicao[1][i])

    glEnd()

def piramide(n,r,h=1):
	base = poligono(n,r)
	lados = poligono(n,r)
	px = 0
	py = 0
	pz = h
	lados.insert(0,[px,py,pz])
        return [lados, base]

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,0,0)
    PiramideBaseN(n=8,r=1)
    glutSwapBuffers()
 
def poligono(n,r):
	pontos = []
	alpha = (2*math.pi)/n
	for i in range(0,n):
		px = r * math.cos(i*alpha)
		py = r * math.sin(i*alpha)
		pz = 0
		pontos.append([px,py,pz])
	return pontos

def timer(i):
    glutPostRedisplay()
    glutTimerFunc((1000/60),timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide Base N")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()

