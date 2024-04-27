import os

import torch

device = "cuda:0" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# env var MODEL_PATH
MODEL_PATH = os.environ.get("LLAMA_MODEL_PATH", "/Users/jamakase/.ollama/models/blobs/sha256-00e1317cbf74d901080d7100f57580ba8dd8de57203072dc6f668324ba545f29")
