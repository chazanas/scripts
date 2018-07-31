import os
import glob

def pull_all(path):

	repos = os.walk(path)
	for r in repos:


if __name__ == '__main__':
	pull_all('~/Projects/')