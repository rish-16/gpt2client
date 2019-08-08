from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M')
gpt2.download_model()

text = gpt2.generate(interactive=True, n_samples=3, return_text=True)
print (text)
