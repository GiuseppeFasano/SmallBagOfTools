import torch 
import nibabel as nib

def tensor2numpy(tensor: torch.Tensor):
    '''Convert torch tensor to numpy.'''
    return tensor.cpu().detach().numpy();