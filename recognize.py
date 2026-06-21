import torch
import torch.nn as nn
import cv2
import os
 HEAD
import matplotlib.pyplot as plt
from torchvision import transforms

# 1. UPDATED: Define the CNN architecture to match your new training script
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.fc = nn.Sequential(
            nn.Linear(64 * 7 * 7, 128), nn.ReLU(), 
            nn.Dropout(0.2),
            nn.Linear(128, 10)
        )

import torch.nn.functional as F
from torchvision import transforms

# 1. Define the exact CNN architecture used during training
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )

        self.fc = nn.Sequential(
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 10)
        )

 1e237dc (add new changes)
    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

 HEAD
# 2. Load the model
model = CNN()
model.load_state_dict(torch.load('mnist_pytorch.pth', weights_only=True))
model.eval()

def predict_digit(image_path):
    if not os.path.exists(image_path):
        return "File not found"

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return "Invalid image"

    # Resize to 28x28
    img = cv2.resize(img, (28, 28))

    # Thresholding: Creates a clean black-and-white image
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)

    # Save the processed image for verification
    plt.imsave(f"processed_{image_path}", img, cmap='gray')

    # Prepare for the model
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    img_tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img_tensor)
        return torch.argmax(output).item()

# 3. Loop through all expected images
print("Starting prediction for digits 0-9...")
for i in range(10):
    filename = f"{i}.png"
    if os.path.exists(filename):
        prediction = predict_digit(filename)
        print(f"The number in {filename} is: {prediction}")
    else:
        print(f"File {filename} not found.")

# 2. Setup model and device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = CNN().to(device)

# Load trained weights
model_path = "data/mnist_pytorch.pth"

if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
else:
    print(f"Error: {model_path} not found. Please train the model first.")
    exit()

# (Not used anymore, but kept if needed later)
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# 3. Predict digits 0-9 located in the data folder
print("Starting prediction for digits 0-9...")

for i in range(10):
    img_path = f"data/{i}.png"

    if os.path.exists(img_path):
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        # Resize to MNIST size
        img = cv2.resize(img, (28, 28))

        # Invert colors (important for downloaded images)
        img = cv2.bitwise_not(img)

        # Convert to tensor
        img_tensor = transforms.ToTensor()(img)
        img_tensor = transforms.Normalize((0.5,), (0.5,))(img_tensor)
        img_tensor = img_tensor.unsqueeze(0).to(device)

        with torch.no_grad():
            output = model(img_tensor)
            prediction = output.argmax(dim=1, keepdim=True).item()

        print(f"Digit {i}.png: Predicted as {prediction}")

    else:
        print(f"File {img_path} not found.")
 1e237dc (add new changes)
