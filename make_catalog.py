#!/usr/bin/python3

import numpy
import glob
import pandas
import argparse
import sqlalchemy 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates STAREPods catalog')
    parser.add_argument('--root', metavar='root', type=str, required=True, 
                        help='the root folder of the pods directory')

    parser.add_argument('--catalog', metavar='catalog', type=str, required=False, default='catalog.sqlite',
                        help='location of catalog')
    
    args = parser.parse_args()
    
    uri = 'sqlite:///{}'.format(args.catalog)
    engine = sqlalchemy.create_engine(uri, echo=False)    
    pods = glob.glob(args.root+ '/*/')
    rows = []
    for pod in pods:        
        chunks = glob.glob(pod + '*.pickle')
        for chunk in chunks:
            row = {}
            row['pod'] = pod.split('/')[-2]
            row['chunk'] = chunk
            row['chunk_name'] = chunk.split('/')[-1]
            row['ts_min'] = pandas.read_pickle(chunk).timestamp.min()
            row['ts_max'] = pandas.read_pickle(chunk).timestamp.max()
            name_parts = chunk.split('/')[-1].split('.')
            row['scan'] = name_parts[0]
            row['satellite'] = name_parts[2]
            row['instrument'] = name_parts[3]
            rows.append(row)
            print(row)
    df = pandas.DataFrame(rows)
    df.to_sql(name='catalog', con=engine, if_exists='replace')
            
            
            
        
        
        
    

