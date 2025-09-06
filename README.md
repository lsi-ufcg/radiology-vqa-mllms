# Radiology VQA using Multimodal LLMs

This project is divided into two modules

## samples-generator

This module generates random samples from a dataset, To allow reproducibility, it supports a seed defined as an environment variable  
For more technical information, see [modules/samples-generator/README.md](modules/samples-generator/README.md)

## mllms

This module passes to the models the imagens and the questions from the dataset, it provides a communication layer with the MLLMs using Langchain  

Supported models:

- GPT 4o  
- Gemini 2.5 Pro  
- Qwen 2.5 VL  
- Llama 3.2 Vision  

It is required to provide some API Keys depending on the model you want to run  

For more technical information, see [modules/mllms/langchain/README.md](modules/mllms/langchain/README.md)

## results

See the [Google Colab notebook](https://colab.research.google.com/drive/1pkybMMYKrbP0uHNmdpf95PcKM6jexABm?usp=sharing) to plot charts and visualize the results  
