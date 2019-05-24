# Simpsons classification

*Classification of Simpsons characters*

## Introduction

This is a simple demo for classifying Simpsons characters with fast.ai and optimizing the neural network by monitoring and comparing runs with Weights & Biases.

Hyper-parameters are defined pseudo-randomly and every run is automatically logged onto [Weighs & Biases](https://www.wandb.com/) for easier analysis/interpretation of results and how to optimize the architecture.

Every single experiment is automatically logged onto [Weighs & Biases](https://www.wandb.com/) for easier analysis/interpretation of results and how to optimize the architecture.

## Usage

1. Install dependencies through `requirements.txt`, `Pipfile` or manually (Pytorch, Fast.ai & Wandb)
2. Log in or sign up for an account -> `wandb login`
3. Run `python train.py`
4. Visualize and compare your runs through generated link

   ![alt text](imgs/results.png)


## Results

After running the script a few times, you will be able to compare quickly a large combination of hyperparameters. As an example, you can refer to [my runs](https://app.wandb.ai/borisd13/simpsons-fastai).

Feel free to modify the script and define your own hyper parameters.