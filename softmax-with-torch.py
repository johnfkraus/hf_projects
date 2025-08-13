import torch
import torch.nn.functional as F

# Example logits tensor
logits = torch.tensor([2.0, 1.0, 0.1])

# Apply softmax using PyTorch's built-in function
probabilities = F.softmax(logits, dim=0)

print("Logits:", logits)
print("Probabilities:", probabilities)
