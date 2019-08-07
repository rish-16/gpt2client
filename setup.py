from distutils.core import setup
import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name = 'gpt2_client',    # How you named your package folder (MyLib)
	packages = ['gpt2_client'],   # Chose the same as "name"
	version = '1.7.3',      # Start with a small number and increase it with every change you make
	license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
	description = 'Easy-to-use Wrapper for GPT-2 117M and 345M Transformer Models',   # Give a short description about your library
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	author = 'Rishabh Anand',                   # Type in your name
	author_email = 'mail.rishabh.anand@gmail.com',      # Type in your E-Mail
	url = 'https://github.com/rish-16/gpt2client',   # Provide either the link to your github or to your website
	download_url = 'https://github.com/rish-16/gpt2client/archive/1.4.tar.gz',    # I explain this later on
	keywords = ['gpt-2', 'wrapper', 'transformer', 'machine learning', 'openai', 'text generation'],   # Keywords that define your package best
	install_requires=[
			'numpy',
			'tensorflow',
			'regex',
			'tqdm',
			'requests',
			'termcolor',
			'functools',
			'gpt_2_simple'
		],
	classifiers=[
	'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
	'Intended Audience :: Developers',      # Define that your audience are developers
	'Topic :: Software Development :: Build Tools',
	'License :: OSI Approved :: MIT License',   # Again, pick a license
	'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	],
)