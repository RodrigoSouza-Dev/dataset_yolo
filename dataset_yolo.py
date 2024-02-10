import fiftyone as fo
from fiftyone import ViewField as F

# Carregar as informações de detecção YOLO de um arquivo JSON
detections = [
    {
        "filepath": "/path/to/image1.jpg",
        "detections": [
            {"label": "person", "bounding_box": [100, 100, 50, 50], "confidence": 0.95},
            {"label": "car", "bounding_box": [200, 200, 80, 40], "confidence": 0.90}
        ]
    },
    {
        "filepath": "/path/to/image2.jpg",
        "detections": [
            {"label": "person", "bounding_box": [50, 50, 60, 60], "confidence": 0.85},
            {"label": "dog", "bounding_box": [150, 150, 70, 70], "confidence": 0.80}
        ]
    },
    # Adicione mais imagens e detecções conforme necessário
]

# Criar um dataset FiftyOne
dataset = fo.Dataset()

# Adicionar amostras ao dataset
for detection in detections:
    sample = fo.Sample(filepath=detection["filepath"])
    
    # Adicionar as detecções YOLO à amostra
    for d in detection["detections"]:
        if "ground_truth" not in sample:
            sample["ground_truth"] = []
        sample["ground_truth"].append(
            fo.Detection(
                label=d["label"],
                bounding_box=d["bounding_box"],
                confidence=d["confidence"]
            )
        )
    
    dataset.add_sample(sample)

# Visualizar o dataset
session = fo.launch_app(dataset)
