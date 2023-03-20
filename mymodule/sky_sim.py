''' A script to simulate a catalogue of simulated stars around Andromeda galaxy '''
import math as mth
import random as rand
import matplotlib.pyplot as plt
# Determine Andromeda location in ra/dec degrees

# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'

# convert to decimal degrees
d, m, s = DEC.split(':')
DEC = int(d)+int(m)/60+float(s)/3600

h, m, s = RA.split(':')
RA = 15*(int(h)+int(m)/60+float(s)/3600)
RA = RA/mth.cos(DEC*mth.pi/180)

# make 1000 stars within 1 degree of Andromeda
NSRC = 1_000_000

ras = []
decs = []
for i in range(NSRC):
    ras.append(RA + rand.uniform(-1,1))
    decs.append(DEC + rand.uniform(-1,1))

# now write these to a csv file for use by my other program
with open('./catalog.csv','w') as f:
    print("id,ra,dec", file=f)
    for i in range(NSRC):
        print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)

plt.scatter(ras[::1000], decs[::1000])
plt.xlabel('RA [deg]')
plt.ylabel('DEC [deg]')
plt.savefig('./plots/sim_star_positions_plot.png')
