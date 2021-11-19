from dqa._dqa import DQA
import os
import time
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

# Feed document and pose questions to DQA

clear = lambda: os.system('cls')
clear()

dqa = DQA()
file_path = '/path/to/context.docx'


dqa.load_file(file_path)
print(f"Loaded file: {file_path}")
#dqa.load_text("This is an example text. Here is another sentence.")

questions = None # Use None for interactive
'''
questions = ['What technology does Mobius use?', \
    'What level of clearance must users of Mobius have?', \
    'What is the data retention period?',\
    'What does the acronym ISSO stand for?',\
    'What application server does Mobius use?', \
    'How many servers does Mobius have?']
'''

@interact
def show_articles_more_than(column='claps', x=5000):
    return df.loc[df[column] > x]

print("START")
print("=================================================================")

done = False
start_all = time.time()

if questions:
    print("Questions hardcoded (AUTO).\n")
    for i, question in enumerate(questions):
        print(f"Question {i}: {question}")
        start = time.time()
        results = dqa.get_answers(question)
        #print("***\n ")
        if not results:
            print(f"No model could determine answer with confidence >= {dqa.MIN_ACCEPTABLE_CONF_SCORE}")
        else:
            for result in results:
                print(f" - {result.model}: (ref: {result.answer} (confidence: {result.score} )")
            
        # Show elapsed
        end = time.time()
        elapsed = end - start
        elapsed_str = time.strftime('%Hh:%Mm:%Ss', time.gmtime(elapsed))
        print(f"Elapsed: {elapsed_str}\n")
else:
    print("Enter question or 'exit' to end.\n")
    while not done:
        question = input("Question: ")
        if question == None or question == 'exit':
            break
        start = time.time()
        results = dqa.get_answers(question)
        if not results:
            print(f"No model could determine answer with confidence >= {dqa.MIN_ACCEPTABLE_CONF_SCORE}")
        else:
            #print("***\n ")
            for result in results:
                print(f" - {result.model}: {result.answer} (confidence: {result.score} )")
            
        # Show elapsed
        end = time.time()
        elapsed = end - start
        elapsed_str = time.strftime('%Hh:%Mm:%Ss', time.gmtime(elapsed))
        print(f"Elapsed: {elapsed_str}\n")

end = time.time()
elapsed_total = end - start_all
elapsed_total_str = time.strftime('%Hh:%Mm:%Ss', time.gmtime(elapsed_total))
print(f"END. Total elapsed: {elapsed_total_str}\n")
    
