import torch.utils
from torch.utils.data import DataLoader
import torchvision, torch
import numpy as np
from torchvision.transforms import v2
from PIL import Image

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
    

# SETUP MODELS
MOBILE_SETUP = {
    "backend": torchvision.models.mobilenet_v3_large(weights=torchvision.models.MobileNet_V3_Large_Weights.DEFAULT),
    "backend_transform": torchvision.models.MobileNet_V3_Large_Weights.DEFAULT.transforms(),
    "weight_path": "weights/alo"
}