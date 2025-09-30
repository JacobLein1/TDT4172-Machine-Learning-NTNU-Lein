import numpy as np

class LogisticRegression: 
  def __init__(self, learning_rate=0.1,epochs =1000):
    self.learning_rate = learning_rate
    self.epochs = epochs
    self.weights, self.bias= None, None
    self.losses, self.train_accuracies= [], []

  def sigmoid_function(self,x):
    return True
  def _compute_loss(self,y, y_pred):
    return True
  def compute_gradients(self,x,y,y_pred):
    return True
  
  def update_parmeters(self, grad_w, grad_b):
    return True
  
  def accuracy(true_values, predictions):
    return np.mean(true_values==predictions)