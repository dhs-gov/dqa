from util import log_util
from util import text_util
import configparser
from transformers import pipeline
import os
import docx2txt
import logging
import warnings
import numpy as np


# Test models
model_0 = pipeline("question-answering", model="deepset/roberta-base-squad2",
                       tokenizer="deepset/roberta-base-squad2")
model_1 = pipeline("question-answering", model="distilbert-base-cased-distilled-squad",
                       tokenizer="distilbert-base-cased-distilled-squad")
model_2 = pipeline("question-answering", model="deepset/electra-base-squad2",
                       tokenizer="deepset/electra-base-squad2")
model_3 = pipeline("question-answering", model="deepset/xlm-roberta-large-squad2",
                       tokenizer="deepset/xlm-roberta-large-squad2")
model_4 = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad",
                       tokenizer="bert-large-uncased-whole-word-masking-finetuned-squad")                    
model_5 = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad",
                       tokenizer="distilbert-base-uncased-distilled-squad")


class DQA():

    # User configurations
    config = None

    # Pipelines list
    pipelines = []

    # Context
    context = ""

    # The minimum confidence score needed to ignore all answers.
    MIN_CONF_SCORE = 1e-2

    # The minimum number of models with MIN_CONF__SCORE needed to ignore all (incorrect) answers.
    MIN_NUM_LOW_CONF_MODELS = 2

    # The minimum confidence score needed to accept as correct answer.
    MIN_ACCEPTABLE_CONF_SCORE = 0.7


    def __init__(self):
        # Read user configuration
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.MIN_CONF_SCORE = self.config['THRESHOLDS']['MIN_CONF_SCORE']
        print(f"MIN_CONF_SCORE: {self.MIN_CONF_SCORE}")

        self.MIN_NUM_LOW_CONF_MODELS = self.config['THRESHOLDS']['MIN_NUM_LOW_CONF_MODELS']
        print(f"MIN_NUM_LOW_CONF_MODELS: {self.MIN_NUM_LOW_CONF_MODELS}")

        self.MIN_ACCEPTABLE_CONF_SCORE = self.config['THRESHOLDS']['MIN_ACCEPTABLE_CONF_SCORE']
        print(f"MIN_ACCEPTABLE_CONF_SCORE: {self.MIN_ACCEPTABLE_CONF_SCORE}")

        # Initialize logger
        log_util.set_logging(self.config)
        # Turn off transformer/numpy warnings
        #log_util.disable_logging()


    def load_file(self, file_path):
        print("Loading file")
        file_ext = os.path.splitext(file_path)[1]
        if file_ext.lower() == '.docx':
            self.context = docx2txt.process(file_path)
        elif file_ext.lower() == '.txt':
            with open(file_path) as f:
                self.context = self.context + f.readlines()


    def determine_correctness(self, model_name, result, answers):

        if not result:
            print("Model is None")
            return None, None
        elif "<s>" in result or "</s>" in result:
            print("Model contains <s>")
            return None, None
        else:
            conf = result.get("score")
            answer = result.get("answer")
            #print(f"  ? {model_name}: {answer} (confidence: {conf} )")
            if conf < float(self.MIN_CONF_SCORE):
                return None, conf
            else:
                if conf > float(self.MIN_ACCEPTABLE_CONF_SCORE):
                    answer = result.get("answer")
                    if not any(answer == x.answer for x in answers):
                        return Result(model_name, result.get("answer"), conf), conf
                    else:
                        #r = Result('model_0', '-----------------', max_false_positive)
                        return None, None
                else:
                    return None, None
                #r.print()


    def get_answers(self, question):
        answers = []
        max_false_positive = 0.00000000000000000001
        num_low_conf_scores = 0

        model_result = model_0(question=question, context=self.context)
        result0, score0 = self.determine_correctness('model_0', model_result, answers)

        if result0 == None and score0:
            num_low_conf_scores+=1

        model_result = model_1(question=question, context=self.context)
        result1, score1 = self.determine_correctness('model_1', model_result, answers)
        if result1 == None and score1:
            num_low_conf_scores+=1

        model_result = model_2(question=question, context=self.context)
        result2, score2 = self.determine_correctness('model_2', model_result, answers)
        if result2 == None and score2:
            num_low_conf_scores+=1

        model_result = model_3(question=question, context=self.context)
        result3, score3 = self.determine_correctness('model_3', model_result, answers)
        if result3 == None and score3:
            num_low_conf_scores+=1

        model_result = model_4(question=question, context=self.context)
        result4, score4 = self.determine_correctness('model_4', model_result, answers)
        if result4 == None and score4:
            num_low_conf_scores+=1

        model_result = model_5(question=question, context=self.context)
        result5, score5 = self.determine_correctness('model_5', model_result, answers)
        if result5 == None and score5:
            num_low_conf_scores+=1

        #print(f"NUM LOW SCORES: {num_low_conf_scores}")
        if num_low_conf_scores < 2:
            if result0:
                answers.append(result0)
                #result0.print()
            if result1:
                answers.append(result1)
                #result1.print()
            if result2:
                answers.append(result2)
                #result2.print()

            if result3:
                answers.append(result3)
                #result3.print()

            if result4:
                answers.append(result4)
                #result4.print()

            if result5:
                answers.append(result5)
                #result5.print()

        num_low_conf_scores = 0
        
        #print("---------------------")

        # To return a new list, use the sorted() built-in function...
        answers.sort(key=lambda x: x.score, reverse=True)
        return answers

class Result:

    model = None
    answer = None
    score = 0.00000000000000000001

    def __init__(self, model, answer, score):
        self.model = model
        self.answer = answer
        self.score = score

    def print(self):
        print(f"  - {self.model}: {self.answer} (confidence: {self.score} )")
