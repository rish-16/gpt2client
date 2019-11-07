<h1 align="center">gpt2-client</h1>

<p align="center">Easy-to-use Wrapper for GPT-2 117M, 345M, 774M, and 1.5B Transformer Models</p>

<p align="center">

  <a>
    <a style="margin: 0 5px" href="https://pypi.org/search/?q=gpt2-client"><img src="https://img.shields.io/pypi/v/gpt2-client?color=%231dd1a1&logo=%231dd1a1&logoColor=%231dd1a1" alt="Pypi package"></a>
  </a>
  <a>
    <a style="margin: 0 5px" href="https://pepy.tech/project/gpt2-client"><img src="https://pepy.tech/badge/gpt2-client" alt="GitHub license"></a>
  </a>
  <a>
    <a style="margin: 0 5px" href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-%23feca57" alt="GitHub license"></a>
  </a>
  <a>
    <a style="margin: 0 5px" href="https://colab.research.google.com/drive/1RZwp1n6XeWxvhBjt1e3ATSOy4Mj9GEEl"><img    src="https://colab.research.google.com/assets/colab-badge.svg"></a>
  </a>

</p>

<p align="center">
  <a style="padding: 0 10px;" href="#what-is-it">What is it</a> • 
  <a style="padding: 0 10px;" href="#installation">Installation</a> • 
  <a style="padding: 0 10px;" href="#getting-started">Getting Started</a>
</p>

<div><img src="https://github.com/rish-16/gpt2client/raw/master/assets/demo.png" /></div>

<p align="center"><strong>Made by Rishabh Anand • <a href="https://rish-16.github.io">https://rish-16.github.io</a></strong></p>

<p align="center"><h2 align="center">What is it</h2></p>

GPT-2 is a Natural Language Processing model [developed by OpenAI](https://openai.com/blog/better-language-models/) for text generation. It is the successor to the GPT (Generative Pre-trained Transformer) model trained on 40GB of text from the internet. It features a Transformer model that was brought to light by the [Attention Is All You Need](https://arxiv.org/abs/1706.03762) paper in 2017. The model has 4 versions - `117M`, `345M`, `774M`, and `1558M` - that differ in terms of the amount of training data fed to it and the number of parameters they contain. 
<br>
<br>
The 1.5B model is currently the largest available model released by OpenAI.
<br>
<br>
Finally, `gpt2-client` is a wrapper around the original [`gpt-2` repository](https://github.com/openai/gpt-2) that features the same functionality but with more accessiblity, comprehensibility, and utilty. You can play around with all three GPT-2 models in less than five lines of code.

> ***Note**: This client wrapper is in no way liable to any damage caused directly or indirectly. Any names, places, and objects referenced by the model are fictional and seek no resemblance to real life entities or organisations. Samples are unfiltered and may contain offensive content. User discretion advised.*

<p align="center"><h2 align="center">Installation</h2></p>

Install client via `pip`. Ideally, `gpt2-client` is well supported for <strong>Python >= 3.5</strong> and <strong>TensorFlow >= 1.X</strong>. Some libraries may need to be reinstalled or upgraded using the `--upgrade` flag via `pip` if *Python 2.X* is used.

```bash
pip install gpt2-client
```

> ***Note:*** `gpt2-client` is **not** compatible with TensorFlow 2.0

<p align="center"><h2 align="center">Getting started</h2></p>

**1. Download the model weights and checkpoints**

```python
from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M') # This could also be `345M`, `774M`, or `1558M`. Rename `save_dir` to anything.
gpt2.load_model(force_download=False) # Use cached versions if available.
```

This creates a directory called `models` in the current working directory and downloads the weights, checkpoints, model JSON, and hyper-parameters required by the model. Once you have called the `load_model()` function, you need not call it again assuming that the files have finished downloading in the `models` directory.

> ***Note:*** Set `force_download=True` to overwrite the existing cached model weights and checkpoints

**2. Start generating text!**

```python
from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M') # This could also be `345M`, `774M`, or `1558M`

gpt2.generate(interactive=True) # Asks user for prompt
gpt2.generate(n_samples=4) # Generates 4 pieces of text
text = gpt.generate(return_text=True) # Generates text and returns it in an array
gpt2.generate(interactive=True, n_samples=3) # A different prompt each time
```

You can see from the aforementioned sample that the generation options are highly flexible. You can mix and match based on what kind of text you need generated, be it multiple chunks or one at a time with prompts.

**3. Generating text from batch of prompts**

```python
from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M') # This could also be `345M`, `774M`, or `1558M`

prompts = [
  "This is a prompt 1",
  "This is a prompt 2",
  "This is a prompt 3",
  "This is a prompt 4"
]

text = gpt2.generate_batch_from_prompts(prompts) # returns an array of generated text
```

**4. Fine-tuning GPT-2 to custom datasets**

```python
from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M') # This could also be `345M`, `774M`, or `1558M`

my_corpus = './data/shakespeare.txt' # path to corpus
custom_text = gpt2.finetune(my_corpus, return_text=True) # Load your custom dataset
```

In order to fine-tune GPT-2 to your custom corpus or dataset, it's ideal to have a GPU or TPU at hand. [Google Colab](http://colab.research.google.com) is one such tool you can make use of to re-train/fine-tune your custom model.

<p align="center"><h2 align="center">Contributing</h2></p>

Suggestions, improvements, and enhancements are always welcome! If you have any issues, please do raise one in the Issues section. If you have an improvement, do file an issue to discuss the suggestion before creating a PR.

All ideas – no matter how outrageous – welcome!

**5. Encoding and decoding text sequences**

```python
from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M') # This could also be `345M`, `774M`, or `1558M`
gpt2.load_model()

# encoding a sentence
encs = gpt2.encode_seq("Hello world, this is a sentence")
# [15496, 995, 11, 428, 318, 257, 6827]

# decoding an encoded sequence
decs = gpt2.decode_seq(encs)
# Hello world, this is a sentence
```

<p align="center"><h2 align="center">Licence</h2></p>

[MIT](https://github.com/rish-16/gpt2client/blob/master/LICENSE.txt)