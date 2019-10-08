"""
The following snippet covers how to use GPT2Client to generate text randomly. 
It will return an array containing the `n_samples` pieces of generated text.
"""

from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M', save_dir="models")

# optional -> if you already have the assets, you can comment this out
gpt2.load_model(force_download=False)

# interative mode is False by default
# This will return 4 pieces of generated text
text = gpt2.generate(n_samples=4, return_text=True)
print (text)