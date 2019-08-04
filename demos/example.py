#!/usr/bin/env python3

from gpt2client import GPT2Client

gpt2 = GPT2Client(model_name='117M')
gpt2.download_model()

text = gpt2.generate(display=False)
print (text)