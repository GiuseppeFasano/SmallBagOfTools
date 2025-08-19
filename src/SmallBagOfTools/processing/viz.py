import numpy as np
import matplotlib.pyplot as plt


class displayer: 
    
    ''' Display set of slices.'''
    
    def __init__(self,
                vol: np.ndarray):
        
        
        self.volume = vol.copy();
        self.current_slice = 0;
        self.nslices = 0; 
        self.ax = None;
    
        self.vmin = self.volume.min();
        self.vmax = self.volume.max();
        
    
    def update_slice(self):
        
        self.ax.imshow(self.volume[:, :, self.current_slice], 
                       cmap='Oranges',
                       vmax = self.vmax,
                       vmin = self.vmin);
        
        plt.title(f"Slice {self.current_slice+1}/{self.nslices}");
        plt.draw()
        print(f"Slice {self.current_slice+1}/{self.nslices}")


    
    def on_scroll(self,event):
        current_slice = self.current_slice;
        num_slices = self.nslices;
        
        if event.button == 'up':
            if current_slice + 1 < num_slices:
                current_slice = current_slice + 1;
        else:
            if current_slice - 1 >= 0:
                current_slice = current_slice - 1;
            
        self.current_slice =  current_slice;
        self.update_slice();
        
        
    def show(self):
        self.nslices = self.volume.shape[-1];
        fig, ax = plt.subplots();
        self.ax = ax;

        self.update_slice();
 
        fig.canvas.mpl_connect('scroll_event', self.on_scroll);
        
        plt.show();


        

