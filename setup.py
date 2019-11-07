from distutils.core import setup
import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
	long_description = f.read()

setup(
	name = 'gpt2_client',
	packages = ['gpt2_client'],
	version = '2.1.3',
	license='MIT',
	description = 'Easy-to-use Wrapper for the GPT-2 117M, 345M, 774M, and 1.5B Transformer Models',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	author = 'Rishabh Anand',
	author_email = 'mail.rishabh.anand@gmail.com',
	url = 'https://github.com/rish-16/gpt2client',
	download_url = 'https://github.com/rish-16/gpt2client/archive/2.1.tar.gz',
	keywords = ['gpt-2', 'AI', 'ML', 'wrapper', 'transformer', 'machine learning', 'openai', 'text generation'],
	install_requires=[
			'numpy',
			'tensorflow',
			'regex',
			'tqdm',
			'requests',
			'termcolor',
			'gpt_2_simple'
		],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
)