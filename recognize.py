import torch
import torch.nn as nn
import cv2
import os
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
    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

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