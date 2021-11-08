# DQA
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Release](https://img.shields.io/badge/release-v0.1-blue)](https://img.shields.io/badge/release-v0.1-blue) [![Version](https://img.shields.io/badge/version-alpha-orange)](https://img.shields.io/badge/version-alpha-orange)

## Quick Start
Open file ```config.ini ``` and set the following parameters: ```LOG_FILE_PATH ``` and 
 ```OUTPUT_DIR ``` for your environment. Next, open file ```example.py``` and change ```file_path``` to point to your 
(context) document. Note that this version currently only supports ```.docx``` files. 

If you want to pose predefined questions, set ```questions``` in ```config.ini ``` to your list of questions:
```
questions = ['What is the subject?', 'Who bought the food?']
```
If you want to pose questions interactively, set ```questions``` in ```config.ini ``` to None:
```
questions = None
```
To run ```example.py```, use:
```
python example.py
```
