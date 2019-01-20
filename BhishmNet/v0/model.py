'''
BhishmAI: model.py

This is the first AI that I am developing for pyfc. The word 'Bhishm' 
comes from the Sanskrit Text Mahabharat, the literal meaning of word 
is the one ot undertakes a terrible vow and completes it. And this is 
also what this AI is, someone who has to undergo terrible things in 
order to prove it's worth.

Sentiments apart, this file contains world's first neural network driven
AI model to play the complete game of freeciv with all the information at
it's hand. Previous attempts at the same work with partial information 
or have many other limitations, not this model!

@yashbonde - 20.01.2019
'''

import tensorflow as tf

from utils.layer_utils import map_placeholder_generator as mpg

class BhishmNet(object):
	def __init__(self, version = 0.0):
		self.version = version

	def build_model(self):
		'''
		function to build the model
		'''

		self.make_map_inputs
		pass

	'''
	BUILD HELPERS
	'''

	def make_map_inputs(self):
		for i in range(self.num_maps):
			setattr(self, 'map_{0}'.format(MAPS[i]), value = mpg(size = MAPSIZE, name = i))