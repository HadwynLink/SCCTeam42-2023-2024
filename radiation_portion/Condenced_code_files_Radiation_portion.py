"""
PLOT GOLD FOIL DEFLECTION(SCATTERING)(CROSS-SECTION)
"""
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

dt = (1.0E-21)*msec#org:1.0E-21

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

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
""""
CSV_CONVERTE.py
PARSE HTE CSV FILE MADE BY GEANT
"""
import csv

#set all of the begining variables to zero  
Total_E_absorbed = 0
Total_E_remaining = 0
num_parts_remaining = 0
num_parts_absorbed = 0
num_parts_reflected = 0

Photo_num = 0
Elect_num = 0
C_num = 0
Mg_num = 0
Proton_num = 0
Ne_num = 0
Alpha_num = 0

Photo_energy = 0
Elect_energy = 0.000
C_energy = 0
Mg_energy = 0
Proton_energy = 0
Ne_energy = 0
Alpha_energy = 0
#
count = 0
count2 = 0
nonabsorbed = 0
Total_E_reflected = 0#not printed (for debugging purposes)

#pick file and open to begin parse
read_directory = '/Users/mario/Dropbox/XimenasWork/super_computing23-24/PILLAR.realthing/radiation/CSV_files/'
read_name = 'Alpha_Kapton_slow.csv'
read_filepath = read_directory + read_name

with open(read_filepath, 'r+') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for columb in csv_reader:
            #convert to readable format
            first_columb = columb[0].split(r" ")
            if str(first_columb[0])[0] != '#':
                    #find_kinetic energy
                    final_k = columb[19].split(r";")
                    #in ke = 0 then particle is absorbed
                    if float(final_k[len(final_k)-1]) == 0.0:
                            num_parts_absorbed += 1
                    else:
                            nonabsorbed +=1
                            #find position 
                            pos = (columb[8].split(r";"))
                            #if position is past barrier then it passes
                            if float(pos[len(pos)-1])>0.01:
                                    num_parts_remaining += 1
                                    Total_E_remaining += float(final_k[len(final_k)-1])
                                    charge = columb[21].split(r";")
                                    pid = columb[6].split(r";") 
                                    #if particle type is photon +1 phtons count
                                    if charge[len(charge)-1] == '0':
                                        Type1 = 'photon'
                                        Photo_energy += float( final_k[len(final_k)-1] )
                                        if float(final_k[len(final_k)-1])>0:
                                                Photo_num += 1
                                    #if part. is electron +1 electron    
                                    if charge[len(charge)-1] == '-1':
                                        Type2 = 'electron'
                                        Elect_Ke = columb[19].split(r";")
                                        Elect_energy += float(final_k[len(final_k)-1])
                                        if float(final_k[len(final_k)-1]) > 0:
                                                Elect_num += 1
                                    #if part. is carbon +1 carbon            
                                    if pid[len(pid)-1] == '1000060120':
                                        Type3 = 'carbon'
                                        C_energy += float(final_k[len(final_k)-1])
                                        if float(final_k[len(final_k)-1]) > 0:
                                                C_num += 1
                                    #if part. is neon +1 neon            
                                    if pid[len(pid)-1] == '1000100200':
                                        Type4 = 'neon'
                                        Ne_energy += float(final_k[len(final_k)-1])
                                        if float(final_k[len(final_k)-1]) > 0:
                                                Ne_num += 1
                                    #if part. is proton +1 proton            
                                    if pid[len(pid)-1] == '2212':
                                        Type5 = 'proton'
                                        Proton_energy += float(final_k[len(final_k)-1])
                                        if float(final_k[len(final_k)-1]) > 0:
                                                Proton_num += 1
                                    #if part. type in mg +1 mg            
                                    if pid[len(pid)-1] == '1000120340':
                                        Type6 = 'magnesium'
                                        Mg_energy += float(final_k[len(final_k)-1])
                                        if float(final_k[len(final_k)-1]) > 0:
                                                Mg_num += 1
                                    else:
                                        Type7 = 'alpha'
                                        Alpha_energy += float(final_k[len(final_k)-1])
                                        if float(final_k[len(final_k)-1]) > 0:
                                                Alpha_num += 1
                            #if position is before barrier then paritcle is reflected                     
                            elif float(pos[len(pos)-1])<-0.000013:
                                    num_parts_reflected += 1
                                    Total_E_reflected += float(final_k[len(final_k)-1])
                            #<.>.<.>.<.>.<.>.<.>. 
                    event_e_absorbed_list = columb[22].split(r";")#remamaining vs absor.
                    #find E absorbed
                    columb_12 = columb[12].split(r";")
                    if columb_12[len(columb_12 )-1]=='0':
                        energy_absorbed = 0
                        count2 += 1 
                    else:
                        energy_absorbed = float(event_e_absorbed_list[0])
                        count += 1
                        #print('particle pass:+1')
                        
                    Total_E_absorbed += energy_absorbed
                    #find resulting particle
#print all variables needed                     
print(read_name, 'read_name','\n',
Total_E_absorbed,'Total_E_absorbed','\n',
Total_E_remaining, 'Total_E_remaining','\n',
num_parts_remaining, 'num_parts_remaining','\n',
num_parts_absorbed,'num_parts_absorbed','\n',
num_parts_reflected,'num_parts_reflected','\n',
'speed','\n',
'dt')

#print remaining particles, type, energy, number
if Photo_num != 0:
        print(Type1,'Type1','\n',
              Photo_num, ' Photo_num', '\n',
              Photo_energy, 'Photo_energy', '\n')

if Elect_num != 0:
        print(Type2,'Type2','\n',
              Elect_num, ' Elect_num', '\n',
              Elect_energy, 'Elect_energy', '\n')
if C_num != 0:
        print(Type3,'Type3','\n',
              C_num, ' C_num', '\n',
              C_energy, 'C_energy', '\n')        
if Ne_num != 0:
        print(Type4,'Type4','\n',
              Ne_num, ' Ne_num', '\n',
              Ne_energy, 'Ne_energy', '\n')
if Proton_num != 0:
        print(Type5,'Type5','\n',
              Proton_num, ' Proton_num', '\n',
              Proton_energy, 'Proton_energy', '\n')
if Mg_num != 0:
        print(Type6,'Type5','\n',
              Mg_num, ' Mg_num', '\n',
              Mg_energy, 'Mg_energy', '\n')
if Alpha_num != 0:
        print(Type7,'Type7','\n',
              Alpha_num, ' Alpha_num', '\n',
              Alpha_energy, 'Alpha_energy', '\n')
print('IGNORE:',(Total_E_absorbed+Total_E_remaining+Total_E_reflected),'total e (KeV)')

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""
K_FINDER.py
"""
#define units
m = 1
km = 1000*m
sec = 1
kg = 1
g = kg/1000

#define mass of particles to be used 
proton_m = (1.67262192E-27)**kg
alpha_m = (6.64465723082E-27)*kg
carbon_m = (1.99E-26)*kg
nitrogen_m = (23.25E-27)*kg
neon_m = (3.35E-26)*kg
magnesium_m = (4.03594014E-26)*kg
beta_m = (9.10938E-31)*kg

#define velocities of the solar wind 
solar_wind_fast = 500*km/sec # fast = 300km/s, fast = 500 km/s
solar_wind_slow = 300*km/sec

#define which variables used for first velocity 
M = alpha_m
v = solar_wind_fast

#find the kinetic energy in Joules 
ke = (1/2)*(M)*(v)**2
#convert to electron volts
eV = ke/1.60217662E-19
print('ev_fast; ', eV)

#define which variables used for second velocity 
v = solar_wind_slow

#find kinetic energy in J
ke = (1/2)*(M)*(v)**2
eV = ke/1.60217662E-19
print('ev_slow; ', eV)

"""
INVERS_SQUARED_LAW.py
asume: foil used is 98cm wide, distance from sun is 1.52au
*find number of parts in a km and a given source
"""
import numpy as np
#defnine units
km = 1
au = 149597870.7*km
sec = 1
hour = 3600*sec
parts = 1 #number of particle as a unit of 1
#define variables(distance, and solar wiand )
r_to_mars = 1.52*au
total_solar_wind = (1.3E36)*(parts/sec)
alpha_per = 0.08 #8% of total solar wind (alpha percentage)
electrons_per = 0.45# beta(-), 45%, electron percentage
gamma_per = 0.005# around 1/2 %

#defining which varables to be used for the invers square law
Luminosity = total_solar_wind
r = r_to_mars
abundance = gamma_per

#find number of part with given luminosity 
num_of_parts = (Luminosity*abundance)/(4*np.pi*(r**2))#(per/s)

#convert to seconds
num_Hit_per_sec = num_of_parts*0.98*sec #(*0.98 cuz of area of blockade)

print('num_Hit_per_sec: ', float(num_Hit_per_sec),'/s')

#given n parts find time step
parts_used = 100_000#specified in programe

dt = parts_used/num_Hit_per_sec

print('dt', dt)

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""
c
"""
:volu world BOX 1*m 0.5*m 0.5*m G4_Galactic

:volu foil(S) BOX 12.5*micrometer 49*cm 49*cm 'Matterial'
:place foil(S) 1 world r000 0*cm 0*cm 0*cm
:color foil(S) 1 1 0 

:rotm r000 0 0 0
:vis world FALSE
###'Material':
#   G4_WATER
#   G4_CONCRETE
#   kapton:
#       :MIXT_BY_NATOMS kapton 1.42E-3 4 C 22 H 10 N 2 O 5
#   G4_Pb
#   G4_Al

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""
Radiation (mac files)
"""
/geometry/source ../'text_geomety_list'.tg
/run/initialize 

/gps/'particle_list'
/gps/energy 'energy_aso'
/gps/pos/centre -50 0 0 cm
/gps/ang/type iso
/gps/ang/minphi 140 deg
/gps/ang/maxphi 220 deg
/gps/ang/mintheta 55 deg
/gps/ang/maxtheta 125 deg

/vis/open VRML2FILE
/vis/drawVolume
/vis/viewer/flush

/vis/scene/add/trajectories
/vis/scene/endOfEventAction accumulate 100000

/analysis/setFileName gears.csv

/run/verbose 2
/run/beamOn 100000
###'text_geomety_list' = tg files condenced ^
###particle_list, energy_aso
#   alpha,      5184 eV

#   alpha,      1866 eV

#   e-,         0.7 eV

#   e-,         0.2558 eV

#   gamma,      110000000 eV

#   gamma,      20000 eV

#/gps/particle ion
#/gps/ion 1 1,        1304.96 eV

#/gps/particle ion
#/gps/ion 1 1,        469.78 eV

#/gps/particle ion
#/gps/ion  6 12,      15525.75 eV

#/gps/particle ion
#/gps/ion  6 12,      5589.2 eV

#/gps/particle ion
#/gps/ion 12 24,      31487.95 eV

#/gps/particle ion
#/gps/ion 12 24,      11335.66 eV

#/gps/particle ion
#/gps/ion 10 20,      26136.3 eV

#/gps/particle ion
#/gps/ion 10 20,      9409 eV
