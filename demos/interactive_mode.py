"""
The following snippet covers how to use GPT2Client interactively. 
The client asks you to enter a prompt `n_samples` times. 

It will return an array containing the generated text for each prompt in order.
"""

from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M', save_dir="models")

# optional -> if you already have the assets, you can comment this out
gpt2.load_model(force_download=False)

text = gpt2.generate(interactive=True, n_samples=4, return_text=True)
print (text)