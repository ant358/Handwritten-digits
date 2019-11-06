# Handwritten Digits Repository
## Experiments with Keras and TensorFlow on the MNIST digits dataset
These experiments aimed to explore the performance of different types of Neural Networks and how to set up their hyperparameters. What is the ideal solution to analysing the standard MNIST digits data set?

### Environment
This work was done in a conda environment on a laptop with a GPU. Using a Jupyter notebooks with nbextensions. If you do not have a GPU, then you will have to install a non-GPU version of TensorFlow.  Or do your experiments in an online environment such as Kaggle or Google Colab.

See PythonGPU.yml for the precise environment I used.
To install this environment on your machine with conda:
'''
conda env create -f PythonGPU.yml
'''
nb. in windows if this doesn't install the packages open the PowerShell or Conda Terminal by right-clicking and selecting 'Run as administrator.'
You can then switch to the environment within Anaconda Navigator or:
'''
conda activate PythonGPU
'''
nb. on Linux use ''' source activate  ''' instead of activate  

I have outputted a requirements.txt for use with pip; it is pervasive and contains everything in the conda environment. 
''' conda list -e > requirements.txt '''  

I haven't tested it, but you could probably get away with reducing it down to items referring to: 
Keras, TensorFlow, pandas, numpy, sklearn and matplotlib. 
