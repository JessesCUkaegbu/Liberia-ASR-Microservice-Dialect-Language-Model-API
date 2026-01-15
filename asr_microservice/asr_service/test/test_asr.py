import torch
from omnilingual_asr.models.inference.pipeline import ASRInferencePipeline

print("Checking device...")
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

print("Loading model...")
pipeline = ASRInferencePipeline.from_pretrained(
    "facebook/omnilingual-asr-7b",
    device=device
)

print("Model loaded successfully!")