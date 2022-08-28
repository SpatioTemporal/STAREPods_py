#!/usr/bin/python3

import numpy
import os
import starepandas
import argparse
import glob
import itertools
import re

import multiprocessing


def list_granules(source, granule_pattern=''):
    granule_paths = sorted(glob.glob(os.path.expanduser(source) + '/' + '*' ))
    pattern = '.*{}.*[^_stare]\.(nc|hdf|HDF5)'.format(granule_pattern)
    granule_paths = list(filter(re.compile(pattern).match, granule_paths))          
    return granule_paths
    
    
def granule_to_pods(granule_path, pod_root, level):
    granule_name = granule_path.split('/')[-1]
    try:
        ds = starepandas.read_granule(granule_path, latlon=True, sidecar=True)
    except ValueError:
        print('could not read {}'.format(granule_path))
        raise ValueError
    if isinstance(ds, dict):    
        for scan in ds:
            df = ds[scan]
            pod_name = scan + '.' + granule_name + '.pickle'
            df.write_pods(pod_root, level, pod_name)            
    elif isinstance(ds, starepandas.STAREDataFrame):
        pod_name = granule_name + '.pickle'
        ds.write_pods(pod_root, level, pod_name)            


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates STAREPods')
    parser.add_argument('--source', metavar='source', type=str, required=True, 
                        help='The granule source folder')    
    parser.add_argument('--pod_root', metavar='root', type=str, required=True, 
                        help='The root folder of the pods directory')
    parser.add_argument('--level', metavar='level', type=int, required=True,
                        help='level/resolution of the pods')    
    parser.add_argument('--pattern', metavar='pattern', type=str, required=False, 
                        help='Pattern of granule file names')
    parser.add_argument('--workers', metavar='workers', type=int, required=False, 
                        help='number of workers')
    
    parser.set_defaults(workers=1)
    parser.set_defaults(pattern='') 
    
    args = parser.parse_args()    
    
    granules = list_granules(args.source, args.pattern)
        
    if args.workers > 1:
        map_args = zip(granules,                        
                       itertools.repeat(args.pod_root),
                       itertools.repeat(args.level))
        with multiprocessing.Pool(processes=args.workers) as pool:
            pool.starmap(granule_to_pods, map_args)
    else:    
        for granule in granules:        
            granule_to_pods(granule, args.pod_root, args.level)   
    
    
