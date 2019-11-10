import tensorflow as tf 
import numpy as np
import pandas as pd
import argparse as ap

def load_model():
	model = tf.keras.models.load_model('domain_classifier_model.h5')
	char2idx = {'-': 0, '.': 1, '0': 2, '1': 3, '2': 4, '3': 5, 
				'4': 6, '5': 7, '6': 8, '7': 9, '8': 10, '9': 11, 
				'_': 12, 'a': 13, 'b': 14, 'c': 15, 'd': 16, 'e': 17, 
				'f': 18, 'g': 19, 'h': 20, 'i': 21, 'j': 22, 'k': 23, 
				'l': 24, 'm': 25, 'n': 26, 'o': 27, 'p': 28, 'q': 29, 
				'r': 30, 's': 31, 't': 32, 'u': 33, 'v': 34, 'w': 35, 
				'x': 36, 'y': 37, 'z': 38}

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

