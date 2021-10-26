import os
import sys
import re
import question_answer
import docx_library
from docx import Document
#import ner
#import keywords
import configparser

def get_token_count(text):
    text_list = re.findall(r"[\w]+|[^\s\w]", text)
    return len(text_list)

if __name__ == '__main__':

    clear = lambda: os.system('cls')
    clear()

    # Read user configuration
    config = configparser.ConfigParser()
    config.read("config.ini")
    x = self.config['SENTIMENT_ANALYSIS']['3_CLASS_POLARITY']


    print("QA Tester")
    # Read document
    file_path = 'C:\\work\\projects\\ai-ml\\qa\\data_test.docx'

    print("Reading file: ", file_path)

    doc = Document(file_path)

    if doc is None:
        print("Doc is null")
        sys.exit()

    docs = []
    text = ""
    print("START")
    for i, paragraph in enumerate(doc.paragraphs):
        print(f"Reading paragraph {i}", end = "\r")
        #highlight = ""
        for run in paragraph.runs:
            if run.font.highlight_color:
                run_token_count = get_token_count(run.text)
                #print(f"run tokens: {run_token_count}")
                text_token_count = get_token_count(text)
                if (run_token_count + text_token_count) > 512:
                    #print(f"total tokens: {run_token_count + text_token_count}")
                    docs.append(text)
                    text = run.text
                else:
                    text += run.text
    # Append remaining text
    print(f"Appending paragraph {i}: {paragraph.text}")
    docs.append(text)

    print("=================================================================")
    print("Enter question or 'exit' to end.\n")

    done = False
    while not done:
        val = input("Question: ")
        if val == 'exit':
            break

        question = val
        results = question_answer.get_answers(question, docs)
        for result in results:
            print(f"  - {result.model}: {result.answer} (confidence: {result.score} )")
        print(f"\n")

    sys.exit()