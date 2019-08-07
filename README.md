<h1 align="center">gpt2-client 🤖📝</h1>

<p align="center">Easy-to-use Wrapper for GPT-2 117M and 345M Transformer Models</p>

<!-- <center>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</center> -->

<img src="https://github.com/rish-16/gpt2client/raw/master/assets/demo.png" style="width: 80%;" />

<p align="center"><strong>Made by Rishabh Anand • <a href="https://rish-16.github.io">https://rish-16.github.io</a></strong></p>

<p aligh="center"><h2 align="center">What is it</h2></p>

GPT-2 is NLP model [developed by OpenAI](https://openai.com/blog/better-language-models/) for text generation. It is the successor to the GPT model trained on 40GB of text from the internet. It features a Transformer model that was brought to light by the [Attention Is All You Need](https://arxiv.org/abs/1706.03762) paper in 2017. The model has two versions - `117M` and `345M` - that differ based on the amount of training data fed to it. 
<br>
<br>
The `345M` model has 1.5 billion parameters and is the largest one yet. Only recently has OpenAI decided to release its training weights as part of its Staged Release plan. There have been several implications and debates over their release plan regarding misuse.
<br>
<br>
Finally, `gpt2-client` is a wrapper around the original [`gpt-2` repository](https://github.com/openai/gpt-2) that features the same functionality but with more accessiblity, comprehensibility, and utilty. You can play around both GPT-2 models with less tha five lines of code.

> ***Note**: This client wrapper is in no way liable to any damage caused directly or indirectly. Any names, places, and objects referenced by the model are fictional and seek no resemblance to real life entities or organisations.*

<p aligh="center"><h2 align="center">Installation</h2></p>

Install client via `pip`. Ideally, `gpt2-client` is well supported for <strong>Python >= 3.5</strong> and <strong>TensorFlow >= 1.X</strong>. Some libraries may need to be reinstalled or upgraded using the `--upgrade` flag via `pip` if *Python 2.X* is used.

```bash
pip install gpt2-client
```

<p aligh="center"><h2 align="center">Getting started</h2></p>

**1. Download the model**

```python
from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M') # This could also be `345M`
gpt2.download_model(save_dir='gpt2-models') # Rename it to anything
```

This creates a directory called `gpt2-models` in the current working directory and downloads the weights, checkpoints, model JSON, and hyper-parameters required by the model. Once you have called the `download_model()` function, you need not call it again assuming that the files have finished downloading in the `gpt2-models` directory.

**2. Start generating text!**

```python
from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M') # This could also be `345M`

gpt2.generate(interactive=True) # Asks user for prompt
gpt2.generate(n_samples=4) # Generates 4 pieces of text
text = gpt.generate(return_text=True) # Generates text and returns it in an array
gpt2.generate(interactive=True, n_samples=3) # A different prompt each time
```

You can see from the aforementioned sample that the generation options are highly flexible. You can mix and match based on what kind of text you need generated, be it multiple chunks or one at a time with prompts.

**3. Fine-tuning GPT-2 to custom datasets**

```python
from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M') # This could also be `345M`

my_corpus = 'shakespeare.txt'
custom_text = gpt2.finetune(my_corpus, return_text=True) # Load your custom dataset
```

In order to fine-tune GPT-2 to your custom corpus or dataset, it's ideal to have a GPU or TPU at hand. [Google Colab](http://colab.research.google.com) is one such tool you can make use of to re-train/fine-tune your custom model.