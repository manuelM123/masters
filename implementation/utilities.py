import os
import sys
import json

'''
Function to read metadata in a genotype format from a file

Parameters:
----------
file : str
    The file to read the metadata from

Returns:
-------
metadata : dict
    The metadata in a dictionary format
'''

def read_metadata(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            metadata = json.load(f)

        f.close()
        return metadata
    else:
        raise FileNotFoundError('File does not exist')

# Function to write metadata to a file in a phenotype format