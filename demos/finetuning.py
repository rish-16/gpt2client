"""
The following snippet covers how to finetune models on custom text datasets (in any language!).
The client returns an array of the generated text.
"""

from gpt2_client import GPT2Client

# optional -> if you already have the assets, you can comment this out
gpt2 = GPT2Client('117M')

my_corpus = './data/shakespeare.txt' # path to corpus
custom_text = gpt2.finetune(my_corpus, return_text=True)
print (custom_text)