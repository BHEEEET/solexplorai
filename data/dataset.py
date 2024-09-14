import torch
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

def get_data_loaders(batch_size):
    # Example data; replace these with actual data loading logic
    train_data = torch.randn(1000, 784)  # Random data for example
    train_labels = torch.randint(0, 10, (1000,))  # Random labels for example
    
    train_dataset = MyDataset(train_data, train_labels)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    
    return train_loader
