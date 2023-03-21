#! /usr/bin/env python
''' 
A script to simulate a catalogue of simulated stars around Andromeda galaxy 
Author: Aman Khalid
Last Change: 20/03/23
'''
import math as mth
import random as rand
import matplotlib.pyplot as plt

NSRC=1_000_000

def get_ra_dec():
    '''
    This function returns the RA and DEC coordinates for the Andromeda galaxy in degrees.
    The returned values are floats.
    '''

    # Determine Andromeda location in ra/dec degrees
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees
    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/mth.cos(dec*mth.pi/180)
    
    return (ra, dec)

def make_stars(ra, dec, NSRC):
    # make 1,000,000 stars within 1 degree of Andromeda

    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(ra + rand.uniform(-1,1))
        decs.append(dec + rand.uniform(-1,1))
    return (ras, decs)

if __name__=='__main__':
    ra, dec = get_ra_dec()
    ras, decs = make_stars(ra, dec, NSRC)
    # now write these to a csv file for use by my other program
    with open('./catalog.csv','w', encoding='utf-8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            f.write(F"{i:07d}, {ras[i]:12f}, {decs[i]:12f}\n")

    plt.scatter(ras[::1000], decs[::1000])
    plt.xlabel('RA [deg]')
    plt.ylabel('DEC [deg]')
    plt.savefig('./plots/sim_star_positions_plot.png')
