 HEAD
# Image Recognition Project

A machine learning project built with PyTorch to recognize handwritten digits.

## Project Overview
This repository contains scripts to train a neural network on the MNIST dataset and perform digit recognition on custom images.

## Project Structure
- `train_pytorch.py`: Script to download the MNIST dataset and train the neural network model.
- `recognize.py`: Script to run inference on new images.
- `requirements.txt`: List of required Python dependencies.
- `data/`: Directory for storing datasets and trained model weights (.pth files).

## Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/acomlilian2000-star/image-recognition.git](https://github.com/acomlilian2000-star/image-recognition.git)
cd image-recognition

# Image Recognition Project: MNIST Digit Classifier

## Project Overview
This repository was developed as a hands-on workshop project to master the fundamentals of Deep Learning using PyTorch. The primary goal was to build an end-to-end pipeline capable of recognizing handwritten digits. By digitizing manual processes, this project explores how machine learning models can be trained to interpret real-world human input.

## Motivation & Objectives
The objective was to move beyond theoretical understanding and implement a practical neural network. Key goals included:
- Establishing a reliable workflow for data preprocessing and image transformation.
- Implementing a robust training loop using PyTorch.
- Creating an intuitive inference mechanism for testing the model against custom user-drawn digits.

## Findings & Key Learnings
Through this project, I identified several critical insights:
- **Data Preprocessing is Paramount**: The model's accuracy is highly dependent on how the input images are resized and normalized to match the MNIST dataset specifications.
- **Model Generalization**: Successfully training a model taught me the importance of hyperparameter tuning, particularly in balancing learning rates and epoch counts to avoid overfitting.
- **Modular Development**: Separating the training logic from the inference script significantly improves maintainability and allows for quicker iterations.

## Project Structure
- `train_pytorch.py`: Handles dataset downloading, training loops, and saving model checkpoints.
- `recognize.py`: Performs inference, allowing users to input images and receive a digit prediction.
- `data/`: Directory for storing datasets and trained model weights (.pth files).
- `requirements.txt`: Project dependencies for environment reproduction.

## Getting Started
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/acomlilian2000-star/image-recognition.git](https://github.com/acomlilian2000-star/image-recognition.git)
   cd image-recognition
)
