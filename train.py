import torch
import torch.nn as nn
import torch.optim as optim
from models.model import SimpleNN
from data.dataset import get_data_loaders

def train_model(num_epochs, learning_rate):
    model = SimpleNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)
    train_loader = get_data_loaders(batch_size=64)

    for epoch in range(num_epochs):
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}')

    torch.save(model.state_dict(), 'model.pth')

if __name__ == "__main__":
    train_model(num_epochs=100, learning_rate=0.01)
