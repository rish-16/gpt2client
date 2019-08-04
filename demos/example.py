from gpt2client import GPT2Client

gpt2 = GPT2Client(model_name='117M')
gpt2.download_model()

gpt2.generate(display=True, interactive=True, n_samples=3)