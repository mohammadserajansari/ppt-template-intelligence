import torch
import torchvision.transforms as T
from PIL import Image

_model = None


def get_vision_model():

    global _model

    if _model is None:
        _model = torch.hub.load(
            "facebookresearch/dino:main",
            "dino_vits16"
        )

    return _model


def get_layout_embedding(image_path):

    model = get_vision_model()

    transform = T.Compose([
        T.Resize((224, 224)),
        T.ToTensor()
    ])

    img = Image.open(image_path)

    with torch.no_grad():
        emb = model(transform(img).unsqueeze(0))

    return emb.numpy()