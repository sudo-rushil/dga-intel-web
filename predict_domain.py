import tensorflow as tf 
import numpy as np
import pandas as pd
import argparse as ap

def load_model():
	model = tf.keras.models.load_model('domain_classifier.h5')
	char2idx = {'-': 0, '.': 1, '0': 2, '1': 3, '2': 4, '3': 5, 
				'4': 6, '5': 7, '6': 8, '7': 9, '8': 10, '9': 11, 
				'a': 12, 'b': 13, 'c': 14, 'd': 15, 'e': 16, 'f': 17, 
				'g': 18, 'h': 19, 'i': 20, 'j': 21,'k': 22, 'l': 23, 
				'm': 24, 'n': 25, 'o': 26, 'p': 27, 'q': 28, 'r': 29, 
				's': 30, 't': 31, 'u': 32, 'v': 33, 'w': 34, 'x': 35, 
				'y': 36, 'z': 37}

	return model, char2idx

def get_arguments():
	parser = ap.ArgumentParser(description='Predict whether a domain name is genuine or not')
	parser.add_argument('domain', type=str, help='The domain to run a prediction on')
	return parser.parse_args()

def get_prediction(model, mapping, domain_name):
  name_vec = [mapping[c] for c in domain_name]
  vec = np.zeros((1, 82))
  vec[0, :len(domain_name)] = name_vec

  prediction = model(vec).numpy().sum()

  return prediction

def main():
	args = get_arguments()
	model, mapping = load_model()

	prediction = get_prediction(model, mapping, args.domain)

	if prediction < 0.5:
		return '\nThe domain {} is genuine with probability {}\n'.format(args.domain, round(1 - prediction, 2))
	else:
	    return '\nThe domain {} is fake with probability {}\n'.format(args.domain, round(prediction, 2))

if __name__ == '__main__':
	output = main()
	print(output)

