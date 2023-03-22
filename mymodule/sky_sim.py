#! /usr/bin/env python
''' 
A script to simulate a catalogue of simulated stars around Andromeda galaxy 
Author: Aman Khalid
Last Change: 20/03/23
'''
import numpy as np
import math as mth
import matplotlib.pyplot as plt
import argparse
import numpy as np

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
    ras = np.random.uniform(size=NSRC,  low=ra-1, high=ra+1)
    decs = np.random.uniform(size=NSRC, low=dec-1, high=dec+1)
    return (ras, decs)

def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser

if __name__=='__main__':
    parser = skysim_parser()
    options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.ra, options.dec]:
        ra, dec = get_ra_dec()
    else:
        ra = options.ra
        dec = options.dec

    ras, decs = make_stars(ra,dec, NSRC)
    # now write these to a csv file for use by my other program

    with open(options.out,'w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    print(f"Wrote {options.out}")

    plt.scatter(ras[::1000], decs[::1000])
    plt.xlabel('RA [deg]')
    plt.ylabel('DEC [deg]')
    plt.savefig('./plots/sim_star_positions_plot.png')
