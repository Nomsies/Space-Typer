from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random as rd
import csv

"""
BUG:
- PELURU TERKADANG MELEWATI METEOR

KEKURANGAN:
- DESAIN KARAKTER DAN LAINNYA
- MENU AWAL
- JUMLAH METEOR DAN PELURU
"""

_txt = []
with open ('word.csv', 'r') as word:
    words = csv.reader(word)
    for txt in words:
        _txt.append(txt)

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
txt_meteor = list(_txt[0][rd.randint(0, len(_txt[0])-1)])

# FUNGSI UNTUK MENAMPILKAN HURUF
def Letter(letter, x):
    glPushMatrix()
    glTranslated(x_meteor + x, y_meteor-50, 0)
    glLineWidth(1.5)
    glBegin(GL_LINES)

    if letter.lower() == 'a':
        glVertex2f( 0.0, 5.0)
        glVertex2f(-2.5,-5.0)
        glVertex2f( 0.0, 5.0)
        glVertex2f( 2.5,-5.0)
        glVertex2f(-1.0, 0.0)
        glVertex2f( 1.0, 0.0)

    elif letter.lower() == 'b':
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-5.0) # | 
        glVertex2f(-2.5,-5.0); glVertex2f( 1.0,-5.0) # _
        glVertex2f(-2.5, 0.0); glVertex2f( 1.0, 0.0) # -
        glVertex2f(-2.5, 5.0); glVertex2f( 1.0, 5.0) # _
        glVertex2f( 2.5,-3.5); glVertex2f( 2.5,-1.5) # |
        glVertex2f( 2.5,-1.5); glVertex2f( 1.0, 0.0) # /
        glVertex2f( 1.0, 0.0); glVertex2f( 2.5, 1.5) # /
        glVertex2f( 2.5, 1.5); glVertex2f( 2.5, 3.5) # |
        glVertex2f( 1.0, 5.0); glVertex2f( 2.5, 3.5) # \
        glVertex2f( 1.0, 0.0); glVertex2f( 1.0,-1.5) # \

    elif letter.lower() == 'c':
        glVertex2f( 2.5, 5.0); glVertex2f(-1.0, 5.0)
        glVertex2f(-1.0, 5.0); glVertex2f(-2.5, 3.5)
        glVertex2f(-2.5, 3.5); glVertex2f(-2.5,-3.5)
        glVertex2f(-2.5,-3.5); glVertex2f(-1.0,-5.0)
        glVertex2f(-1.0,-5.0); glVertex2f( 2.5,-5.0)

    elif letter.lower() == 'd':
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-5.0) # |
        glVertex2f(-1.0,-5.0); glVertex2f(-2.5,-5.0) # _
        glVertex2f(-1.0,-5.0); glVertex2f( 2.5,-3.5) # /
        glVertex2f( 2.5,-3.5); glVertex2f( 2.5, 3.5) # |
        glVertex2f( 1.0, 5.0); glVertex2f( 2.5, 3.5) # \
        glVertex2f( 1.0, 5.0); glVertex2f(-2.5, 5.0) # _

    elif letter.lower() == 'e':
        glVertex2f(-2.5, 5.0); glVertex2f( 2.5, 5.0)
        glVertex2f(-2.5, 0.0); glVertex2f( 2.5, 0.0)
        glVertex2f(-2.5,-5.0); glVertex2f( 2.5,-5.0)
        glVertex2f(-2.5,-5.0); glVertex2f(-2.5, 5.0)

    elif letter.lower() == 'f':
        glVertex2f(-2.5, 5.0); glVertex2f( 2.5, 5.0)
        glVertex2f(-2.5, 0.0); glVertex2f( 3.5, 0.0)
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-5.0)

    elif letter.lower() == 'g':
        glVertex2f( 2.5, 5.0); glVertex2f(-1.0, 5.0)
        glVertex2f(-1.0, 5.0); glVertex2f(-2.5, 3.5)
        glVertex2f(-2.5, 3.5); glVertex2f(-2.5,-3.5)
        glVertex2f(-2.5,-3.5); glVertex2f(-1.0,-5.0)
        glVertex2f(-1.0,-5.0); glVertex2f( 1.0,-5.0)
        glVertex2f( 1.0,-5.0); glVertex2f( 2.5,-3.5)
        glVertex2f( 2.5,-3.5); glVertex2f( 2.5, 0.0)
        glVertex2f( 2.5, 0.0); glVertex2f( 0.0, 0.0)

    elif letter.lower() == 'h':
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-5.0)
        glVertex2f(-2.5, 0.0); glVertex2f( 2.5, 0.0)
        glVertex2f( 2.5, 5.0); glVertex2f( 2.5,-5.0)
    
    elif letter.lower() == 'i':
        glVertex2f( 0.0, 5.0); glVertex2f( 0.0,-5.0)
    
    elif letter.lower() == 'j':
        glVertex2f(-2.5, 0.0); glVertex2f(-2.5,-3.5)
        glVertex2f(-2.5,-3.5); glVertex2f(-1.0,-5.0) 
        glVertex2f( 1.0,-5.0); glVertex2f(-1.0,-5.0) 
        glVertex2f( 2.5,-3.5); glVertex2f( 1.0,-5.0) 
        glVertex2f( 2.5, 5.0); glVertex2f( 2.5,-3.5)

    elif letter.lower() == 'k':
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-5.0)
        glVertex2f(-2.5, 0.0); glVertex2f( 2.5, 5.0)
        glVertex2f(-2.5, 0.0); glVertex2f( 2.5,-5.0)

    elif letter.lower() == 'l':
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-5.0)
        glVertex2f( 2.5,-5.0); glVertex2f(-2.5,-5.0)
    
    elif letter.lower() == 'm':
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-5.0)
        glVertex2f(-1.25, 0.0); glVertex2f(-2.5, 5.0)
        glVertex2f( 1.25, 0.0); glVertex2f( 2.5, 5.0)
        glVertex2f( 2.5, 5.0); glVertex2f( 2.5,-5.0)

    elif letter.lower() == 'n':
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-5.0)
        glVertex2f( 2.5, 5.0); glVertex2f( 2.5,-5.0)
        glVertex2f(-2.5, 5.0); glVertex2f( 2.5,-5.0)

    elif letter.lower() == 'o':
        glVertex2f(-2.5, 3.5); glVertex2f(-2.5,-3.5)
        glVertex2f(-2.5, 3.5); glVertex2f(-1.0, 5.0)
        glVertex2f(-2.5,-3.5); glVertex2f(-1.0,-5.0)
        glVertex2f( 1.0,-3.5); glVertex2f(-1.0,-3.5)
        glVertex2f( 1.0, 3.5); glVertex2f(-1.0, 3.5)
        glVertex2f( 2.5, 3.5); glVertex2f( 2.5,-3.5)
        glVertex2f( 2.5, 3.5); glVertex2f( 1.0, 5.0)
        glVertex2f( 2.5,-3.5); glVertex2f( 1.0,-5.0)

    elif letter.lower() == 'p':
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-5.0)
        glVertex2f(-2.5, 5.0); glVertex2f( 1.5, 5.0)
        glVertex2f(-2.5, 0.0); glVertex2f( 1.5, 0.0)
        glVertex2f( 2.5, 3.5); glVertex2f( 1.5, 3.5)
        glVertex2f( 2.5, 1.5); glVertex2f( 1.5, 0.0)
        glVertex2f( 2.5, 1.5); glVertex2f( 2.5, 3.5)

    elif letter.lower() == 'q':
        glVertex2f(-2.5, 3.5); glVertex2f(-2.5,-3.5)
        glVertex2f(-2.5, 3.5); glVertex2f(-1.0, 5.0)
        glVertex2f(-2.5,-3.5); glVertex2f(-1.0,-5.0)
        glVertex2f( 1.0,-3.5); glVertex2f(-1.0,-3.5)
        glVertex2f( 1.0, 3.5); glVertex2f(-1.0, 3.5)
        glVertex2f( 2.5, 3.5); glVertex2f( 2.5,-3.5)
        glVertex2f( 2.5, 3.5); glVertex2f( 1.0, 5.0)
        glVertex2f( 2.5,-3.5); glVertex2f( 1.0,-5.0)
        glVertex2f( 0.0, 0.0); glVertex2f(-2.5,-5.0)
    
    elif letter.lower() == 'r':
        glVertex2f(-2.5, 5.0)
        glVertex2f(-2.5,-5.0) #
        glVertex2f(-2.5, 5.0)
        glVertex2f( 1.0, 5.0) #
        glVertex2f( 1.0, 5.0)
        glVertex2f( 2.5, 3.5) #
        glVertex2f( 2.5, 3.5)
        glVertex2f( 2.5, 1.5) #
        glVertex2f( 2.5, 1.5)
        glVertex2f( 1.0, 1.5) #
        glVertex2f( 1.0, 1.5)
        glVertex2f(-2.5, 0.0) #
        glVertex2f( 2.5,-1.5)
        glVertex2f( 2.5,-5.0)
    
    elif letter.lower() == 's':
        glVertex2f( 2.5, 5.0); glVertex2f(-1.0, 5.0) # _
        glVertex2f(-2.5, 3.5); glVertex2f(-1.0, 5.0)
        glVertex2f(-2.5, 3.5); glVertex2f(-2.5, 1.5)
        glVertex2f(-1.0, 0.0); glVertex2f(-2.5, 1.5)
        glVertex2f(-1.0, 0.0); glVertex2f( 1.0, 0.0) # _
        glVertex2f( 1.0, 0.0); glVertex2f( 2.5,-1.5)
        glVertex2f( 2.5,-3.5); glVertex2f( 2.5,-1.5)
        glVertex2f( 2.5,-3.5); glVertex2f( 1.0,-5.0)
        glVertex2f(-2.5,-5.0); glVertex2f( 1.0,-5.0) # _
    
    elif letter.lower() == 't':
        glVertex2f(-2.5, 5.0); glVertex2f( 2.5, 5.0)
        glVertex2f( 0.0, 5.0); glVertex2f( 0.0,-5.0)

    elif letter.lower() == 'u':
        glVertex2f(-2.5, 5.0); glVertex2f(-2.5,-3.5)
        glVertex2f(-2.5,-3.5); glVertex2f(-1.0,-5.0) 
        glVertex2f( 1.0,-5.0); glVertex2f(-1.0,-5.0) 
        glVertex2f( 2.5,-3.5); glVertex2f( 1.0,-5.0) 
        glVertex2f( 2.5, 5.0); glVertex2f( 2.5,-3.5)
        
    elif letter.lower() == 'v':
        glVertex2f(-2.5, 5.0); glVertex2f( 0.0,-5.0)
        glVertex2f( 2.5, 5.0); glVertex2f( 0.0,-5.0)
        
    elif letter.lower() == 'w':
        glVertex2f(-2.5, 5.0); glVertex2f(-1.25,-5.0)
        glVertex2f( 0.0, 5.0); glVertex2f(-1.25,-5.0)
        glVertex2f( 0.0, 5.0); glVertex2f( 1.25,-5.0)
        glVertex2f( 2.5, 5.0); glVertex2f( 1.25,-5.0)
        
    elif letter.lower() == 'x':
        glVertex2f(-2.5, 5.0); glVertex2f( 2.5,-5.0)
        glVertex2f( 2.5, 5.0); glVertex2f(-2.5,-5.0)
        
    elif letter.lower() == 'y':
        glVertex2f(-2.5, 5.0); glVertex2f( 0.0, 0.0)
        glVertex2f( 2.5, 5.0); glVertex2f( 0.0, 0.0)
        glVertex2f( 0.0, 0.0); glVertex2f( 0.0,-5.0)
        
    elif letter.lower() == 'z':
        glVertex2f(-2.5, 5.0); glVertex2f( 2.5, 5.0)
        glVertex2f( 2.5, 5.0); glVertex2f(-2.5, 5.0)
        glVertex2f(-2.5,-5.0); glVertex2f( 2.5,-5.0)
    
    glEnd()
    glPopMatrix()

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
    global y_satelite, x_meteor, y_meteor, x_bullet, y_bullet, col_bullet, trg_bullet, trg_satelite, txt_meteor
    x_meteor -= 0.5
    
    # APABILA METEOR TERKENA PELURU (POSISI PELURU DAN METEOR SAMA)
    if x_bullet in range(int(x_meteor-25), int(x_meteor+25)):
        col_bullet = True
        x_meteor, y_meteor = 1025, rd.randint(75, 650) # SPAWN ULANG METEOR
        x_bullet, y_bullet = 50, y_satelite # SPAWN ULANG PELURU
        col_bullet = False
        trg_bullet, trg_satelite = True, True
    
    if len(txt_meteor) == 0:
        trg_satelite = False
        mov_satelite()
        txt_meteor = list(_txt[0][rd.randint(0, len(_txt[0])-1)])

# FUNGSI PERPINDAHAN PELURU
def mov_bullet(value = 0):
    global x_bullet, y_bullet
    if trg_bullet == False:
        x_bullet += 2
        
        # PERULANGAN FUNGSI "mov_bullet" SAAT "trg_bullet" = False
        glutTimerFunc(1, mov_bullet, value)

# FUNGSI UNTUK TOMBOL KEYBOARD
def Control(key, x, y):
    global x_bullet, y_bullet, trg_bullet, trg_satelite, txt_meteor

    if key == b' ':
        trg_satelite = False
        mov_satelite()

    if key == txt_meteor[0].encode():
        txt_meteor.pop(0)
    print(txt_meteor)

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
    
    pos_letter = len(txt_meteor) / 2

    for i in txt_meteor:
        Letter(i, (txt_meteor.index(i)-pos_letter)*7.5)

    if col_bullet == False:
        Bullet()
        Meteor()
        mov_meteor()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
glutCreateWindow("Space Typer")
glutDisplayFunc(showScreen)
glutKeyboardFunc(Control)
glutIdleFunc(showScreen)
glutMainLoop()