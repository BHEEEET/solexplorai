import torch
from models.model import SimpleNN
from data.dataset import get_data_loaders

def evaluate_model():
    model = SimpleNN()
    model.load_state_dict(torch.load('model.pth', weights_only=True))
    model.eval()
    test_loader = get_data_loaders(batch_size=64)

    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    print(f'Accuracy: {accuracy}%')

if __name__ == "__main__":
    evaluate_model()
