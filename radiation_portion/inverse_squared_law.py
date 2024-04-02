"""
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
#<><><><><><><><><><><><><><><><><><><><><><>
#given n parts find time step
parts_used = 100_000#specified in programe

dt = parts_used/num_Hit_per_sec

print('dt', dt)
