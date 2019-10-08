"""
The following snippet covers how to pass in prompts using a list. The client iterates through the prompts and returns
and array containing the generated text pertaining to each prompt.
"""

from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M', save_dir="models")

# optional -> if you already have the assets, you can comment this out
gpt2.load_model(force_download=False)

prompts = [
    "Today is a beautiful day",
    "Today was a very bad day"
]

text = gpt2.generate_batch_from_prompts(prompts)
print (text)