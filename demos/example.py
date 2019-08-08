from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M')
gpt2.download_model()

gpt2.generate(interactive=True)
