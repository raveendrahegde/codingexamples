# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
#
# Given the following formula,
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * √(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
#
# Write a program to read in the data files from disk, it must then print the names
# of bipedal dinosaurs from fastest to slowest. Do not print any other information.

# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore

# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal

def speed(sl, ll):
    return speed
    
def dino_speed()
    import csv
    file1='dataset1.csv'
    file2='dataset2.csv'
    
    file1content=csv.reader(file1)
    file2content=csv.reader(file1)
    
    dino_details={}
    
    for line in file1content:
        dino_detalis[line[0]] = {'sl': line[1], 'st': line[2]}
    for line in file2content:
        if line[0] in dino_detalis:
            dino_detalis[line[0]]['ll'] = line[1]
            dino_detalis[line[0]]['diet'] = line[2]
        else:
            dino_detalis[line[0]] = {'ll': line[1], 'diet': line[2]}
        
    for key, val in dino_detalis.iteritems():
        speed = speed(val[ll], val[ll])
        
    
    
    
