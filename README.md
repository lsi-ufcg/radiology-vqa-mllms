# Radiology VQA using Multimodal LLMs

This project is divided into two modules

## samples-generator

This module generates random samples from a dataset, To allow reproducibility, it supports a seed defined as an environment variable  
For more technical information, see [modules/samples-generator/README.md](modules/samples-generator/README.md)

## mllms

This module provides a communication layer with MLLMs using Langchain to evaluate the results.

For more technical information, see [modules/mllms/langchain/README.md](modules/mllms/langchain/README.md)

## results

See the [Google Colab notebook](https://colab.research.google.com/drive/1pkybMMYKrbP0uHNmdpf95PcKM6jexABm?usp=sharing) to plot charts and visualize the results
