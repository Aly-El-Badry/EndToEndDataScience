import pickle 
import sklearn 
import argparse
from numpy import exp

try : 
    lr = pickle.load(open('../artifacts/lr.pkl', 'rb'))
except Exception as e : 
    print(e)



argparse = argparse.ArgumentParser(description= "this model to predict bike share ")

argparse.add_argument('--values','-v', nargs='+', type=float )

argparse.add_argument('--name')

args = argparse.parse_args()


pred = lr.predict([args.values])

print(exp(pred)[0])