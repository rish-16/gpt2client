from gpt2_client import GPT2Client

def main():
	my_gpt2 = GPT2Client(model_name='117M')
	my_gpt2.download_model()

	gpt2.generate(display=True, interactive=True, n_samples=1)
	
	dataset = './my_data/shakespeare.txt'
	custom_text = my_gpt2.finetune(dataset, return_text=True)

	print (custom_text)

if __name__ == '__main__':
	main()