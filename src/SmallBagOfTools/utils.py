import os
import torch
import random
import numpy as np


def set_seed(seed: int = 82):
    
    ''' Set seed for reproducibility '''
    
    np.random.seed(seed);
    torch.manual_seed(seed);
    torch.cuda.manual_seed(seed);
    torch.cuda.manual_seed_all(seed);
    torch.backends.cudnn.deterministic = True;
    random.seed(seed);
    
    
def get_device(device: int = None,
               verbose: bool = True):

    ''' Returns available device for training '''
    
    if torch.cuda.is_available():
        
        
        if device is not None:
            if verbose:
                print(f"\n[!] Using requested GPU {device}.");
        
            return device(f"cuda:{device}");
        else:
            if verbose:
                print(f"\n[!] Using available GPU.");
                
            return device(torch.cuda.current_device()); 
    
    else:
        print("\n[!] Using CPU.");
        return device("cpu");
    
    
def check_folder(path: str):
    
    ''' Check if folder exist or create it '''
    
    if not os.path.isdir(path):
        print(f"\n[i] {path} created.")
        os.mkdir(path);
    else:
        print(f"\n[i] {path} already exists.")