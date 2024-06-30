import torch.utils
from torch.utils.data import DataLoader
import torchvision, torch
import numpy as np
from torchvision.transforms import v2
from PIL import Image
from os import sys
from torchvision import transforms,models
from torch import cuda, nn

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


def predict_image(
    model,
    image_path,
    class_names=["indoor", "outdoor"],
):
    preprocess = transforms.Compose(
        [
            transforms.Resize(560),
            transforms.CenterCrop(560 - 24),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    image = Image.open(image_path)
    image_tensor = preprocess(image).unsqueeze(0)
    device = cuda.device("cuda") if cuda.is_available() else "cpu"

    with torch.no_grad():
        model = model.to(device)
        output = model(image_tensor)

    _, predicted = torch.max(output, 1)

    # print(f'Predicted class: {class_names[predicted.item()]}')
    # print(predicted.item())
    return class_names[predicted.item()]


def predict_environment(imagepath):
    model = models.mobilenet_v3_large(weights="DEFAULT")
    num_classes = 2
    model.classifier = nn.Sequential(
        nn.Linear(in_features=960, out_features=1280, bias=True),
        nn.Hardswish(),
        nn.Dropout(p=0.2),
        nn.Linear(in_features=1280, out_features=num_classes, bias=True),
    )
    map_loc = cuda.device("cuda") if cuda.is_available() else "cpu"
    model.load_state_dict(
        torch.load("models-indoor-outdoor/best_model.pth", map_location=map_loc)
    )
    pred = predict_image(model, imagepath)
    # print(f"Predicted class: {pred}")
    return pred


"""
Expected behavior:
    python scene.py grocery.png
"""
if __name__ == "__main__":
    imagepath = sys.argv[1]

    pred = infer(model, imagepath, CLASSES)
    pred_env = predict_environment(imagepath)
    print(f"Prediction: {pred} - {pred_env}")
