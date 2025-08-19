import os
import pandas as pd
from typing import Union


def read_dataframe(path: str):
    
    '''
        Read dataframe depending on extenction.
    '''
    
    if path.endswith(".tsv"):
        return pd.read_csv(path, sep='\t'); 
    else:
        return pd.read_csv(path);
    
    
class summaryManager:
    
    ''' 
        Check previous work and update it.
        
        -> path: path/to/dataframe (without extension)
    '''
    
    def __init__(self,
                path: str):
        
        self.path = f"{path}.csv";
        
        self.summary = None;
        self.start_idx = None;

        self._init_data();
    
    
    def _init_data(self):
        
        if os.path.isfile(self.path):
            print("\n[!] Pregressed work found.");
            summary = read_dataframe(self.path);
            start_idx = summary.shape[0];
            print(f"[i] Already done: {start_idx}\n     Restarting from {start_idx+1}.");

        else:
            print("\n[X] No pregressed work found."); 
            summary = pd.DataFrame();
            start_idx = 0;
        
        self.summary = summary;
        
    
    def _update_with_dict(seld, data: dict):
        if summary.shape[0] != 0:
            summary.loc[summary.shape[0]] = data;
        
        else:       
            summary = pd.DataFrame(data, index=[0]);


    def _update_with_dataframe(seld, data: pd.DataFrame):
        if summary.shape[0] != 0:
            summary = pd.concat([summary, data]).reset_index(drop = True); 
        else:       
            summary = data.copy(deep = True);      
    
    
    def get_start_index(self):
        return self.start_idx;
    
    
    def update(self, data: Union[dict, pd.DataFrame]):
        if isinstance(data, dict):
            self._update_with_dict(data);
        else:
            self._update_with_dataframe(data);
    
    
    def save(self):
        self.summary.to_csv(self.summary, index = False);
    

     