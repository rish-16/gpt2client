from gpt2_client import GPT2Client

gpt2 = GPT2Client('117M')
gpt2.load_model(force_download=True)

prompts = ["hello", "world", "this is a prompt"]
gpt2.generate_batch_from_prompts(prompts)