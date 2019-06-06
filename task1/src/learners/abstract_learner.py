from abc import ABC, abstractmethod

from task1.src.garcon import Garcon
from task1.src.preprocces_data import TweetsPreProcessor
import matplotlib.pyplot as plt

gc = Garcon()

class AbstractLearner(ABC):
	@abstractmethod
	def __init__(self, X_train, y_train):
		self.prep = TweetsPreProcessor(X_train)
		self.X_train = self.prep.processTweets(X_train)
		self.y_train = y_train
		self.classifier_name=''

	@abstractmethod
	def set_name(self):
		pass

	@abstractmethod
	def classify(self, X):
		pass

	@abstractmethod
	def report(self, X, y):
		pass
