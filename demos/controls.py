"""
The following snippet covers how to control the specifics of the generated text.
With GPT2Client, you can control the number of words generated (for now).
"""

from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M', save_dir="models")

# optional -> if you already have the assets, you can comment this out
gpt2.load_model(force_download=False)

# returns a body of text 40 words in length
text = gpt2.generate(words=40)
print (text)