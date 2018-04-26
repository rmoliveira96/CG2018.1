from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys

def esfera(r,lat,lon):
    vert = []
    inct = (2*math.pi)/lat
    incf = math.pi/lat
    for i in range(0,lat,1):
        glBegin(GL_LINE_STRIP)
        vert[0] = 0
        vert[1] = 0
        vert[2] = -r
        glVertex3fv(vert)
        
        for j in range(0,lon,1):
            vert[0] = r*cos(i*inct)*(cos(j*incf-0.5*math.pi)
            vert[1] = r*sin(i*inct)*(cos(j*incf-0.5*math.pi)
            vert[2] = r*sin(j*incf-0.5*math.pi)
            glVertex3fv(vert)
            vert[0] = r*cos((i+1)*inct)*cos(j*incf-0.5*math.pi)
            vert[1] = r*sin((i+1)*inct)*cos(j*incf-0.5*math.pi)
            glVertex3fv(vert)

        vert[0] = 0
        vert[1] = 0
        vert[2] = r
        glVertex3fv(vert)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    esfera(2,50,50);
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
	glViewport(0,0,w,h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45,float(w)/float(h),0.1,50.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0,1,10,0,0,0,0,1,0)

def init():
	mat_ambient = (0.6, 0.0, 0.0, 1.0)
	mat_diffuse = (1.0, 0.0, 0.0, 1.0)
	mat_specular = (1.0, 1.0, 1.0, 1.0)
	mat_shininess = (50,)
	light_position = (5.0, 5.0, 5.0, 0.0)
	glClearColor(0.0,0.0,0.0,0.0)
	glShadeModel(GL_SMOOTH)

	glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_MULTISAMPLE)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,600)
	glutCreateWindow("Esfera")
	init()
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutTimerFunc(50,timer,1)
	glutMainLoop()

main()


