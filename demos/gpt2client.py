import os
from termcolor import colored, cprint
import requests
import sys
from tqdm import tqdm

class GPT2Client(object):
	def __init__(self, model_size='117M'):
		self.model_size = model_size

	def download_model(self):
		if self.model_size not in ['117M', '345M']:
			raise AssertionError('Please choose from either 117M or 345M parameter models only. This library does support other model sizes.')
		else:
			subdir = os.path.join('models', self.model_size)
			if not os.path.exists(subdir):
				os.makedirs(subdir)
			
			for filename in ['checkpoint','encoder.json','hparams.json','model.ckpt.data-00000-of-00001', 'model.ckpt.index', 'model.ckpt.meta', 'vocab.bpe']:
				r = requests.get('https://storage.googleapis.com/gpt-2/' + subdir + "/" + filename, stream=True)

				with open(os.path.join(subdir, filename), 'wb') as f:
					file_size = int(r.headers['content-length'])
					chunk_size = 1000
					with tqdm(ncols=100, desc='Downloading {}'.format(colored(filename, 'cyan', attrs=['bold'])), total=file_size, unit_scale=True) as pbar:
						for chunk in r.iter_content(chunk_size=chunk_size):
							f.write(chunk)
							pbar.update(chunk_size)

	def generate_random_sample(self, top_k=40):
