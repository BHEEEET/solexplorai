import torch

# Load the state dictionary or checkpoint from the .pth file
state_dict = torch.load('model.pth', weights_only=True)

# Print the keys to see the names of parameters
print("Keys in the state_dict:")
for key in state_dict.keys():
    print(key)

# Print the size of each parameter sdf
print("\nParameter sizes:")
for key, value in state_dict.items():
    print(f'{key}: {value.size()}')