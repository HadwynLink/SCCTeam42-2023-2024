#copied from read_write file.
""""
parse the csv file made by geant
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
####

