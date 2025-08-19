import torch
from torch import device, nn


def load_model(model: nn.Module,
            path: str,
            device: device = device("cpu"),
            eval_mode: bool = False):

    ''' Load pretrained moel '''

    model.load_state_dict(torch.load(path, map_location = torch.device(device.type)));
    model.to(device);

    if eval_mode:
        print("\n[i] Setting torch model to EVALUATION mode.");
        model.eval();
    else:
        print("\n[i] Setting torch model to TRAINING mode.");
        model.train();
        
    return model;


def save_model(model: nn.Module,
               path: str):
    ''' Save torch model to path. '''
    torch.save(model.state_dict(), path);