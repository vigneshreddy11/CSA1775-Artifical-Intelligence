import torch
import torch.nn as nn

# Define a simple feedforward neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 3)  # 2 input features, 3 output classes
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        return self.softmax(self.fc1(x))

# Create and set model parameters manually
model = SimpleNN()
model.fc1.weight.data = torch.tensor([[0.5, -0.5], [-0.5, 0.5], [0.5, 0.5]])
model.fc1.bias.data = torch.tensor([0.1, -0.1, 0.2])

# Get user input and make a prediction
user_input = list(map(float, input("Enter two input features: ").split()))
prediction = model(torch.tensor([user_input], dtype=torch.float32))
predicted_class = torch.argmax(prediction).item()

print(f"Predicted class: {predicted_class}")

