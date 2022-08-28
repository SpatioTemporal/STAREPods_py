#!/usr/bin/python3

import numpy
import os
import pystare
import argparse


def get_sids(level):
    level_increment = pystare.spatial_increment_from_level(level)
    n_trixels = 8 * (4 ** level)
    r_ = numpy.arange(n_trixels)
    sids = r_ * level_increment+level    
    return sids


def hex16(i):
    return "0x%016x"%i


def make_folders(rootdir, sids):
    for sid in sids:
        os.mkdir('{rootdir}/{sid}'.format(rootdir=rootdir, sid=sid))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates STAREPods Folder Structure')
    parser.add_argument('--folder', metavar='folder', type=str, required=True, 
                        help='the root folder of the pods directory')
    parser.add_argument('--hex', required=False, default=True, action='store_true', 
                        help='toggle using hex instead of int64')    
    parser.add_argument('--level', metavar='level', type=int, required=True,
                        help='level/resolution of the pods')    
    
    args = parser.parse_args()
    
    sids = get_sids(args.level)
    
    if hex:
        sids = list(map(hex16, sids))
        
    make_folders(args.folder, sids)
