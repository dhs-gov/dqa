# DQA
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Release](https://img.shields.io/badge/release-v0.1-blue)](https://img.shields.io/badge/release-v0.1-blue)

## Installation
To install with pypi, use:
```
pip install dqa
```

## Quick Start
Open file ```example.py``` and change ```file_path``` to point to your 
(context) document. Note that this version currently only supports ```.docx``` files. 

If you want to use predefined questions, set ```questions``` to list of questions:
```
questions = ['What is the subject?', 'Who bought the food?']
```
If you want to pose questions interactively, set ```questions``` to None:
```
questions = None
```
To run ```example.py```, use:
```
python example.py
```
