from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

def PrismaBaseN(n,r):

    #BAIXO
    glBegin(GL_POLYGON)
    glColor3f(0,1,1)
    posicao = prisma(n,r)    
    for i in range(n):
	glVertex3f(posicao[1][i][0],posicao[1][i][1],posicao[1][i][2])
    glEnd()

    #LATERAIS
    glBegin(GL_QUAD_STRIP)
    glColor3f(1,0,1)
    for i in range(n):
	glVertex3f(posicao[0][i][0],posicao[0][i][1],posicao[0][i][2])
	glVertex3f(posicao[0][i][0],posicao[0][i][1],posicao[0][i][2]+2)
    glEnd()

    #CIMA
    glBegin(GL_POLYGON)
    for i in range(n):
	glColor3f(0,1,1)
	glVertex3f(posicao[1][i][0],posicao[1][i][1],posicao[1][i][2]+2)
    glEnd()

def prisma(n,r,h=2):
	base = poligono(n,r)
	lados = poligono(n,r)
#	px = r
#	py = r
#	pz = h
#	lados.insert(0,[px,py,pz])
        return [lados, base]

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,0,0)
    PrismaBaseN(n=9,r=1)
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
glutCreateWindow("Prisma Base N")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()

