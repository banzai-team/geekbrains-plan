import os

import torch

device = "cuda:0" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# env var MODEL_PATH
MODEL_PATH = os.environ.get("LLAMA_MODEL_PATH", None)