#last edited 11-4
##START DIS. STAYS THE SAME

import numpy as np
import math as M
import pygame as pg
import time 
import matplotlib.pyplot as plt

from pygame.locals import (
  KEYDOWN,
  K_ESCAPE,
  QUIT,
)

##constance and variables
pi = np.pi
m = 1
km = 1000*m
fm = (1E-16)*m
kg = 1
amu = (1.67377E-27)*kg
sec = 1
msec = (1E-3)*sec
minute = 60*sec
hour = 60*minute
day = 24*hour
newtons = (kg*m)/(sec**2)
C = 1
c_light = 299_792_458*(m/sec)
q_proton = (1.6E-19)*C
k = (8.99)*(10E9)*newtons*(m**2 )/(C**2)
#################
dt = (1.0E-21)*msec#org:1.0E-21
#################
scale = 15*fm ##km/pixel
shift = 300
degree = pi/180 # CD
red = (255,0,0)
blue = (0,0,255)
purple = (102,0,102)
white = (255,255,255)
HIGHT = -50000#0000

##pygame setup
#pg.init()
#scr = pg.display.set_mode([500,500])
#pg.display.set_caption('RutherfordScattering.py')
#my_font = pg.font.SysFont('Verdana', 15)
#done = False

##read and write file/s
directory = '/Users/mario/Dropbox/XimenasWork/python practice/'
name = 'Gold_foil_angleVShight'

THETA_Y = []
HIGHT_X = []
    

filepath = directory + name
def Start():
    ##mass and r of Au and He
    Au_m = 197*amu
    Au_r = 7.5*fm#7.5*fm
    Au_q = 79*q_proton
    He_m = 4*amu
    He_r = 1.1*fm
    He_q = 2*q_proton

    Au_r_old = np.array([0,0,0])
    Au_v_old = np.array([0,0,0])

    He_r_old = np.array([1000*fm,HIGHT*fm,0])
    He_v_old = np.array([-c_light/20,0,0])
    start_v = He_v_old
    t = 0

    min_len = 2000*fm
    globals().update(locals())
    
Start()

#pg.draw.line(scr, 'green', ((Au_r_old[0]/scale)+shift,(Au_r_old[1]/scale)+shift),((Au_r_old[0]/scale)+shift,(Au_r_old[1]/scale)+shift),4)
#pg.draw.line(scr, 'red',   ((He_r_old[0]/scale)+shift,(He_r_old[1]/scale)+shift),((He_r_old[0]/scale)+shift,(He_r_old[1]/scale)+shift),1)
#pg.display.flip()   

for Hight in range(-1000,1000):
    Start()
    for trial in range(0,15000):
        #elliptical orbit
        rAu_He = Au_r_old - He_r_old
        rAu_He_length = M.sqrt(np.inner(rAu_He,rAu_He))
              
        rAu_He_hat = rAu_He/rAu_He_length

        if rAu_He_length <= 4*fm:
            print("particles have crashed")
            
            break
        if He_v_old.all() > 0:
            print('This works#')#quit()

        F = -k*(Au_q*He_q)*rAu_He_hat/(rAu_He_length)**2
        F1 = He_v_old

        #a of He & Au
        Au_a_old = -F/Au_m
        He_a_old = F/He_m


        #r of obj. 1,2,3
        Au_r_new = Au_r_old + Au_v_old*dt
        He_r_new = He_r_old + He_v_old*dt

        #v of obj.1,2,3
        Au_v_new = Au_v_old + Au_a_old*dt
        He_v_new = He_v_old + He_a_old*dt
        
        #text_surface = my_font.render('* Green-Gold *red-Helium', False, white)
        #scr.blit(text_surface,(0,0))
        #pg.draw.line(scr, 'green', ((Au_r_old[0]/scale)+shift,(Au_r_old[1]/scale)+shift),((Au_r_new[0]/scale)+shift,(Au_r_new[1]/scale)+shift),5)
        #pg.draw.line(scr, 'red',   ((He_r_old[0]/scale)+shift,(He_r_old[1]/scale)+shift),((He_r_new[0]/scale)+shift,(He_r_new[1]/scale)+shift),5)
        
        Au_r_old = Au_r_new
        He_r_old = He_r_new
        
        Au_v_old = Au_v_new
        He_v_old = He_v_new

        t = t + dt
        #pg.display.flip()
        #if trial%1 == 0:
        #   scr.fill((0,0,0))
        #for event in pg.event.get():
        #    if event.type == KEYDOWN:
        #        if event.key == K_ESCAPE:
        #            Start()
        if min_len>rAu_He_length:
            min_len = rAu_He_length

       
    end_v = He_v_old
    theta = np.arccos(( np.inner(start_v,end_v) )/( (np.linalg.norm(start_v)*np.linalg.norm(end_v) ) ))
    #print("theta = ", theta/degree)
    print(HIGHT)
    HIGHT_X.append(HIGHT)
    THETA_Y.append(theta/degree)
    HIGHT = 50*Hight 
plt.plot(HIGHT_X,THETA_Y)
plt.title('GoldFoilEx')
plt.xlabel("Hight")
plt.ylabel("Theta")
plt.show()
print('done')
