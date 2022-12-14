from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random as rd
import csv
from time import time
import math
import time as t
"""
BUG :
- TULISAN GAME OVER TIDAK TIDAK TEPAT

KEKURANGAN:
- DESAIN KARAKTER DAN LAINNYA
- MENU AWAL
"""

# MENGAMBIL DATA DARI 'Word.csv' UNTUK DIJADIKAN TEKS METEOR
_txt = []
with open('word.csv', 'r') as word:
    words = csv.reader(word)
    for txt in words:
        _txt.append(txt)

play = False  # PENENTU MULAI GAME

# SEBAGAI PENCATAT WAKTU (Timer[0] : WAKTU START GAME dan Timer[1] : WAKTU INGAME)
Timer = [None, None, 0, 0, 0]

satelite = [0, 350, False]  # TITIK KOORDINAT & TRIGGER SATELIT

# TITIK KOORDINAT, KOLISION DAN TRIGGER BULLET
bullet = [50, 350, False, False]
# TITIK KOORDINAT, KOLISION DAN TRIGGER BULLET
bullet1 = [50, 350, False, False]
# TITIK KOORDINAT, KOLISION DAN TRIGGER BULLET
bullet2 = [50, 350, False, False]

# TITIK KOORDINAT, TEKS METEOR & SHOW TEKS
meteor = [1025, rd.randint(75, 675), True]
# TITIK KOORDINAT, TEKS METEOR & SHOW TEKS
meteor1 = [1025, rd.randint(75, 675), True]
# TITIK KOORDINAT, TEKS METEOR & SHOW TEKS
meteor2 = [1025, rd.randint(75, 675), True]

speed = 0.02

txt_meteor = list(_txt[0][rd.randint(0, len(_txt[0])-1)])
txt_meteor1 = list(_txt[0][rd.randint(0, len(_txt[0])-1)])
txt_meteor2 = list(_txt[0][rd.randint(0, len(_txt[0])-1)])


satelite_color1 = 169, 169, 169
satelite_color2 = 255, 255, 255
satelite_color3 = 94, 211, 246
satelite_color4 = 188, 168, 37

meteor_color = 165, 165, 165


def square(x, y, height, width, color):
    glBegin(GL_POLYGON)
    glColor3ub(color[0], color[1], color[2])
    height = height/2
    width = width/2
    glVertex2f(-width+x, height+y)
    glVertex2f(width+x, height+y)
    glVertex2f(width+x, -height+y)
    glVertex2f(-width+x, -height+y)
    glEnd()

def round():
    glPushMatrix()
    glColor3ub(145, 145, 145)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glTranslated(2, 14, 0)
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 10 * math.cos(theta)
        y = 10 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glColor3ub(145, 145, 145)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glTranslated(-10, -25, 0)
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 7 * math.cos(theta)
        y = 7 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glColor3ub(145, 145, 145)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glTranslated(10, -10, 0)
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 4 * math.cos(theta)
        y = 4 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glPopMatrix()

# FUNGSI MENAMPILKAN SATELIT
def Satelite():
    glPushMatrix()
    glColor3f(1.0, 2.0, 1.5)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glTranslated(satelite[0], satelite[1], 0)
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 50 * math.cos(theta)
        y = 50 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glColor3ub(24,154,180)  # WARNA SATELIT 188, 168, 37
    # POSISI PERPINDAHAN SATELIT BERADA
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 48 * math.cos(theta)
        y = 48 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glColor3f(1.0, 2.0, 1.5)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 45 * math.cos(theta)
        y = 45 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glColor3ub(24,154,180)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 30 * math.cos(theta)
        y = 30 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glColor3f(1.0, 2.0, 1.5)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 20 * math.cos(theta)
        y = 20 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glColor3ub(24,154,180)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glTranslated(20, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(0, 5)
    glVertex2f(50, 5)
    glVertex2f(50, -5)
    glVertex2f(0, -5)
    glEnd()
    glColor3ub(24,154,180)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 5 * math.cos(theta)
        y = 5 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glColor3ub(24,154,180)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glTranslated(50, 0,0)
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 5 * math.cos(theta)
        y = 5 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    glColor3ub(255,255,255)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    # glTranslated(20, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(0, 3)
    glVertex2f(-48, 3)
    glVertex2f(-48, -3)
    glVertex2f(0, -3)
    glEnd()
    glColor3ub(255,255,255)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 3 * math.cos(theta)
        y = 3 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glColor3ub(255,255,255)  # WARNA SATELIT
    # POSISI PERPINDAHAN SATELIT BERADA
    glTranslated(-50, 0,0)
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        x = 3 * math.cos(theta)
        y = 3 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glPopMatrix()

   


# FUNGSI MENAMPILKAN BULLET
def Bullet(x, y):
    glColor3f(1.0, 0.0, 0.0)  # WARNA BULLET
    glPushMatrix()
    glTranslated(x, y, 0)  # POSISI PERPINDAHAN BULLET

    # BENTUK BULLET
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = 2 * 3.1415926*i/360
        a = 5 * math.cos(theta)
        b = 5 * math.sin(theta)
        glVertex2f(a, b)
    glEnd()
    glPopMatrix()

# FUNGSI MENAMPILKAN METEOR


def Meteor(x, y):
    glPushMatrix()
    glColor3ub(165, 165, 165)  # WARNA METEOR
    glTranslated(x, y, 0)  # POSISI PERPINDAHAN METEOR

    # BENTUK METEOR
    glBegin(GL_POLYGON)
    glVertex2f(0, 30)
    glVertex2f(5.9, 29.6)
    glVertex2f(11.9, 27.6)
    glVertex2f(22.3, 23)
    glVertex2f(26.2, 15.1)
    glVertex2f(28.5, 4.96)
    glVertex2f(26.4, -4.5)
    glVertex2f(19.8, -13.9)
    glVertex2f(18.3, -21.8)
    glVertex2f(9.44, -28.02)
    glVertex2f(0, -30)
    glVertex2f(-7.9, -27.6)
    glVertex2f(-18.7, -23.6)
    glVertex2f(-26.4, -19.5)
    glVertex2f(-30.7, -12.15)
    glVertex2f(-32.3, -5.07)
    glVertex2f(-31.08, 5.6)
    glVertex2f(-26.06, 13.8)
    glVertex2f(-24.8, 21.17)
    glVertex2f(-14.4, 24.4)
    glVertex2f(-11.5, 30.19)
    glVertex2f(-4.9, 33.1)
    glEnd()
    round()
   
    glPopMatrix()

# FUNGSI PERPINDAHAN SATELIT


def mov_satelite(value=0):
    global satelite, bullet, txt_meteor, txt_meteor1, txt_meteor2

    if bullet[1] != meteor[1] and len(txt_meteor) == 1:
        bullet[1] = meteor[1]
        bullet1[1] = meteor[1]
        bullet2[1] = meteor[1]
        satelite[1] = meteor[1]

    if bullet1[1] != meteor1[1] and len(txt_meteor1) == 1:
        bullet[1] = meteor1[1]
        bullet1[1] = meteor1[1]
        bullet2[1] = meteor1[1]
        satelite[1] = meteor1[1]

    if bullet2[1] != meteor2[1] and len(txt_meteor2) == 1:
        bullet[1] = meteor2[1]
        bullet1[1] = meteor2[1]
        bullet2[1] = meteor2[1]
        satelite[1] = meteor2[1]

    # APABILA POSISI SATELIT SEJAJAR DENGAN METEOR
    if bullet[1] == meteor[1] and len(txt_meteor) == 1:
        bullet[2] = False
        mov_bullet()

    if bullet1[1] == meteor1[1] and len(txt_meteor1) == 1:
        bullet1[2] = False
        mov_bullet()

    if bullet2[1] == meteor2[1] and len(txt_meteor2) == 1:
        bullet2[2] = False
        mov_bullet()

    # PERULANGAN FUNGSI "mov_satelite" SAAT "trg_satelite" = False
    if satelite[2] == False:
        glutTimerFunc(10, mov_satelite, value)

# FUNGSI PERPINDAHAN METEOR


def mov_meteor():
    global satelite, meteor, bullet, txt_meteor, txt_meteor1, txt_meteor2
    meteor[0] -= speed
    meteor1[0] -= speed
    meteor2[0] -= speed

    # APABILA METEOR TERKENA BULLET (POSISI BULLET DAN METEOR SAMA)
    if (bullet[0] in range(int(meteor[0]-25), int(meteor[0]+25)) or bullet[0] >= meteor[0]) and bullet[1] == meteor[1]:
        bullet[3] = True
        meteor[0], meteor[1] = 1025, rd.randint(75, 650)  # SPAWN ULANG METEOR
        bullet[0], bullet[1] = 50, satelite[1]  # SPAWN ULANG BULLET
        bullet[3] = False
        bullet[2], satelite[2] = True, True
        txt_meteor = list(_txt[0][rd.randint(0, len(_txt[0])-1)])

    # APABILA METEOR1 TERKENA BULLET1 (POSISI BULLET1 DAN METEOR1 SAMA)
    if (bullet1[0] in range(int(meteor1[0]-25), int(meteor1[0]+25)) or bullet1[0] >= meteor1[0]) and bullet1[1] == meteor1[1]:
        bullet1[3] = True
        meteor1[0], meteor1[1] = 1025, rd.randint(
            75, 650)  # SPAWN ULANG METEOR
        bullet1[0], bullet1[1] = 50, satelite[1]  # SPAWN ULANG BULLET
        bullet1[3] = False
        bullet1[2], satelite[2] = True, True
        txt_meteor1 = list(_txt[0][rd.randint(0, len(_txt[0])-1)])

    # APABILA METEOR2 TERKENA BULLET2 (POSISI BULLET2 DAN METEOR2 SAMA)
    if (bullet2[0] in range(int(meteor2[0]-25), int(meteor2[0]+25)) or bullet2[0] >= meteor1[0]) and bullet2[1] == meteor2[1]:
        bullet2[3] = True
        meteor2[0], meteor2[1] = 1025, rd.randint(
            75, 650)  # SPAWN ULANG METEOR
        bullet2[0], bullet2[1] = 50, satelite[1]  # SPAWN ULANG BULLET
        bullet2[3] = False
        bullet2[2], satelite[2] = True, True
        txt_meteor2 = list(_txt[0][rd.randint(0, len(_txt[0])-1)])

    # APABILA TEKS METEOR HABIS
    if len(txt_meteor) == 1:
        meteor[2] = False
        satelite[2] = False
        mov_satelite()

    # APABILA TEKS METEOR1 HABIS
    if len(txt_meteor1) == 1:
        meteor1[2] = False
        satelite[2] = False
        mov_satelite()

    # APABILA TEKS METEOR2 HABIS
    if len(txt_meteor2) == 1:
        meteor2[2] = False
        satelite[2] = False
        mov_satelite()

    # APABILA POSISI METEOR 1025
    if meteor[0] == 1025:
        meteor[2] = True

    # APABILA POSISI METEOR1 1025
    if meteor1[0] == 1025:
        meteor1[2] = True

    # APABILA POSISI METEOR1 1025
    if meteor2[0] == 1025:
        meteor2[2] = True

# FUNGSI PERPINDAHAN BULLET


def mov_bullet():
    global bullet, bullet1, bullet2
    # KONDISI AGAR BULLET DITEMBAKKAN
    if bullet[2] == False:
        bullet[0] += 1

    # KONDISI AGAR BULLET1 DITEMBAKKAN
    if bullet1[2] == False:
        bullet1[0] += 1

    # KONDISI AGAR BULLET2 DITEMBAKKAN
    if bullet2[2] == False:
        bullet2[0] += 1

# FUNGSI UNTUK TOMBOL KEYBOARD


def Control(key, x, y):
    global bullet, satelite, txt_meteor, txt_meteor1, txt_meteor2, play

    # MENGAMBIL INPUTAN KEYBOARD SAAT INGAME
    if play is True:
        if key == txt_meteor[0].encode() and len(txt_meteor) > 1:
            txt_meteor.pop(0)
        if key == txt_meteor1[0].encode() and len(txt_meteor1) > 1:
            txt_meteor1.pop(0)
        if key == txt_meteor2[0].encode() and len(txt_meteor2) > 1:
            txt_meteor2.pop(0)

    # MENGAMBIL INPUTAN KEYBOARD SAAT GAME TIDAK DIMULAI
    else:
        # TEKAN 'R' UNTUK MEMULAI GAME
        if key == b' ':
            play = True

        # TEKAN SPACE UNTUK KELUAR APLIKASI
        if key == b'q':
            glutDestroyWindow(main)

# FUNGSI UNTUK MENGUBAH FORMAT WAKTU UNTUK DITAMPILKAN


def Convert_Time(sec):
    global Timer
    mins = sec // 60    # MINUTES
    sec = sec % 60      # SECONDS
    hours = mins // 60  # HOURS
    mins = mins % 60    # MINUTES
    Timer[2], Timer[3], Timer[4] = hours, mins, sec
    return (f"Time : {int(hours)}.{int(mins)}.{int(sec)}")


def showScreen():
    global Timer, play, meteor, speed
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1000, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1000, 0, 700, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if play == True:
        # MENIGISI WAKTU START
        # titik()
        if Timer[0] is None:
            Timer[0] = time()

        # MEMPERBARUI WAKTU YANG TELAH DILALUI DALAM GAME
        Timer[1] = time()
        pTime = Convert_Time(Timer[1]-Timer[0])  # KONVERSI FORMAT WAKTU

        if Timer[3] % 1 == 0 and Timer[4] % 60 == 0:
            speed += 0.15
            print('tambah')

        # MENAMPILKAN WAKTU YANG TELAH DILALUI
        glPushMatrix()
        glColor3ub(255, 255, 22)
        pos_letter = (len(pTime)-1) / 2
        glRasterPos2d(475, 650)
        for i in pTime:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i.upper()))
        glPopMatrix()

        # MENAMPILKAN TEKS METEOR
        pos_letter = (len(txt_meteor)-1) / 2
        glPushMatrix()
        if len(txt_meteor) > 1:
            glColor3ub(255, 144, 205)
            glRasterPos2d(meteor[0] + (-pos_letter)*11, meteor[1]-50)
            for i in txt_meteor:
                glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i.upper()))
        glPopMatrix()

        pos_letter1 = (len(txt_meteor1)-1) / 2
        glPushMatrix()
        if len(txt_meteor1) > 1:
            glColor3ub(255, 144, 205)
            glRasterPos2d(meteor1[0] + (-pos_letter1)*9, meteor1[1]-50)
            for i in txt_meteor1:
                glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i.upper()))
        glPopMatrix()

        pos_letter2 = (len(txt_meteor)-1) / 2
        glPushMatrix()
        if len(txt_meteor2) > 1:
            glColor3ub(255, 144, 205)
            glRasterPos2d(meteor2[0] + (-pos_letter2)*9, meteor2[1]-50)
            for i in txt_meteor2:
                glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i.upper()))
        glPopMatrix()

        if bullet[3] == False:
            Bullet(bullet[0], bullet[1])
            Bullet(bullet1[0], bullet1[1])
            Bullet(bullet2[0], bullet2[1])
            Meteor(meteor[0], meteor[1])
            Meteor(meteor1[0], meteor1[1])
            Meteor(meteor2[0], meteor2[1])
            mov_meteor()

        # KONDISI GAME OVER
        if satelite[0] == meteor[0] or satelite[0] == meteor1[0] or satelite[0] == meteor2[0]:
            play = False

        Satelite()

    # MENAMPILKAN SCENE GAME OVER
    else:
        glPushMatrix()
        text = "SPACE TYPER"
        glColor3ub(230, 94, 54)
        glRasterPos2f(450, 300)
        for i in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

        developer = "Dikembangkan oleh :\n1. FAISAL BAHARI\n2. SILVI MAULANI\n3. REOFALDO MICHELANGELO LAU"
        glRasterPos2f(450, 280)
        line = 0
        for i in developer:
            if i == '\n':
                line += 1
                glRasterPos2f(450, 280 - 20*line)
            else:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(i))
        glPopMatrix()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 700)
glutInitWindowPosition(0, 0)
main = glutCreateWindow("Space Typer")
glutDisplayFunc(showScreen)
glutKeyboardFunc(Control)
glutIdleFunc(showScreen)
glutMainLoop()
