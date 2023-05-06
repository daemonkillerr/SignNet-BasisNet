"""
    File to load dataset based on user control from main file
"""

from data.molecules import MoleculeDataset
from dgl.data import ZINCDataset

def LoadData(DATASET_NAME):
    """
        This function is called in the main.py file 
        returns:
        ; dataset object
    """
    
    # handling for (ZINC) molecule dataset
    if DATASET_NAME == 'ZINC' or DATASET_NAME == 'ZINC-full':
        return ZINCDataset()
