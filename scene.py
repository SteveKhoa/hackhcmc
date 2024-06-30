import torch.utils
from torch.utils.data import DataLoader
import torchvision, torch
import numpy as np
from torchvision.transforms import v2
from PIL import Image
from os import sys

class SceneModel(torch.nn.Module):
    def __init__(
        self,
        backend_model,
        backend_transforms,
        output_length,
    ):
        super(SceneModel, self).__init__()

        backend_model.fc = torch.nn.Linear(
            backend_model.fc.in_features,
            output_length,
        )
        self.model = backend_model

        self.transforms = backend_transforms

    def forward(self, x):
        x = x.float() / 255
        x = self.transforms(x)
        logits = self.model.forward(x)
        return logits

class MobileSceneModel(torch.nn.Module):
    def __init__(
        self,
        backend_model,
        backend_transforms,
        output_length,
    ):
        super(MobileSceneModel, self).__init__()

        backend_model.classifier[-1] = torch.nn.Linear(
            backend_model.classifier[-1].in_features,
            output_length
        )
        self.model = backend_model

        self.transforms = backend_transforms

    def forward(self, x):
        x = x.float() / 255
        x = self.transforms(x)
        logits = self.model.forward(x)
        return logits
    

# ASSUMPTION
CLASSES = ['bar-pub', 'grocery', 'restaurant', 'supermarket']

# SETUP MODELs
backend = torchvision.models.mobilenet_v3_large(weights=torchvision.models.MobileNet_V3_Large_Weights.DEFAULT)
backend_transform = torchvision.models.MobileNet_V3_Large_Weights.DEFAULT.transforms()
model = MobileSceneModel(backend, backend_transform, len(CLASSES))
weight_path = "weights/standard.pth"  # can use either augmented.pth or standard.pth
state_dict = torch.load(weight_path, map_location=torch.device('cpu'))
model.load_state_dict(state_dict)

# SETUP infer
def infer(model, path, classes):
    model.eval()
    with torch.no_grad():
        image = torchvision.io.read_image(path, mode=torchvision.io.ImageReadMode.RGB)
        image = image.unsqueeze(0)
        logits = model.forward(image)

        argmax = torch.argmax(logits, dim=1)
        pred = classes[argmax]
    
    return pred


"""
Expected behavior:
    python scene.py grocery.png
"""
if __name__ == "__main__":
    imagepath = sys.argv[1]

    pred = infer(model, imagepath, CLASSES)
    print("Prediction: {}".format(pred))