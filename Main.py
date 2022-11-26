from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random as rd

# TITIK KOORDINAT, KOLISION, DAN TRIGGER SATELIT
x_satelite, y_satelite = 50, 250
col_satelite = False
trg_satelite = False

# TITIK KOORDINAT, KOLISION DAN TRIGGER PELURU
x_bullet, y_bullet = 50, 250
col_bullet = False
trg_bullet = False

# TITIK KOORDINAT DAN TEKS METEOR
x_meteor, y_meteor = 1025, rd.randint(50,675)

# FUNGSI MENAMPILKAN SATELIT
def Satelite():
    glColor3f(1.0, 2.0, 1.5) # WARNA SATELIT
    glPushMatrix()
    glTranslated(x_satelite, y_satelite, 0) #POSISI PERPINDAHAN SATELIT BERADA
    
    # BENTUK SATELIT
    glBegin(GL_POLYGON)
    glVertex(-25, -25)
    glVertex(-25, 25)
    glVertex(25, 25)
    glVertex(25, -25)
    glEnd()
    glPopMatrix()

# FUNGSI MENAMPILKAN PELURU
def Bullet():
    global x_bullet, y_bullet
    glColor3f(1.0, 0.0, 0.0) # WARNA PELURU
    glPushMatrix()
    glTranslated(x_bullet, y_bullet, 0) # POSISI PERPINDAHAN PELURU

    # BENTUK PELURU
    glBegin(GL_POLYGON)
    glVertex2f(-5, -5)
    glVertex2f(-5, 5)
    glVertex2f(5, 5)
    glVertex2f(5, -5)
    glEnd()
    glPopMatrix()

# FUNGSI MENAMPILKAN METEOR
def Meteor():
    glColor3f(2.0, 0.75, 0.23) # WARNA METEOR
    glPushMatrix()
    glTranslated(x_meteor, y_meteor, 0) # POSISI PERPINDAHAN METEOR

    # BENTUK METEOR
    glBegin(GL_POLYGON)
    glVertex2f(-25, -25)
    glVertex2f(-25, 25)
    glVertex2f(25, 25)
    glVertex2f(25, -25)
    glEnd()
    glPopMatrix()

# FUNGSI PERPINDAHAN SATELIT
def mov_satelite(value = 0):
    global y_satelite, y_meteor, y_bullet, trg_bullet

    # APABILA POSISI SATELIT LEBIH TINGGI DARI METEOR
    if y_satelite > y_meteor:
        y_bullet -= 1
        y_satelite -= 1

    # APABILA POSISI SATELIT LEBIH RENDAH DARI METEOR
    elif y_satelite < y_meteor:
        y_bullet += 1
        y_satelite += 1

    # APABILA POSISI SATELIT SEJAJAR DENGAN METEOR
    else:
        trg_bullet = False
        mov_bullet()

    # PERULANGAN FUNGSI "mov_satelite" SAAT "trg_satelite" = False
    if trg_satelite == False:
        glutTimerFunc(10, mov_satelite, value)

# FUNGSI PERPINDAHAN METEOR
def mov_meteor():
    global p_input, y_satelite, x_meteor, y_meteor, x_bullet, y_bullet, col_bullet, trg_bullet, trg_satelite
    x_meteor -= 0.5
    
    # APABILA METEOR TERKENA PELURU (POSISI PELURU DAN METEOR SAMA)
    if x_bullet in range(int(x_meteor-25), int(x_meteor+25)):
        col_bullet = True
        x_meteor, y_meteor = 1025, rd.randint(50, 675) # SPAWN ULANG METEOR
        x_bullet, y_bullet = 50, y_satelite # SPAWN ULANG PELURU
        col_bullet = False
        trg_bullet, trg_satelite = True, True
        
# FUNGSI PERPINDAHAN PELURU
def mov_bullet(value = 0):
    global x_bullet, y_bullet
    if trg_bullet == False:
        x_bullet += 2
        
        # PERULANGAN FUNGSI "mov_bullet" SAAT "trg_bullet" = False
        glutTimerFunc(1, mov_bullet, value)

def Control(key, x, y):
    global p_input, x_bullet, y_bullet, trg_bullet, trg_satelite

    if key == b' ':
        trg_satelite = False
        mov_satelite(0)
    if key == b'a':
        p_input = 'a'
    if key == b'b':
        p_input = 'b'
    if key == b'c':
        p_input = 'c'
    if key == b'd':
        p_input = 'd'

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1000, 0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    Satelite()
    if col_bullet == False:
        Bullet()
        Meteor()
        mov_meteor()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
glutCreateWindow("Star Track")
glutDisplayFunc(showScreen)
glutKeyboardFunc(Control)
glutIdleFunc(showScreen)
glutMainLoop()