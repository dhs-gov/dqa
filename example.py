from dqa._dqa import DQA
import os
import time

clear = lambda: os.system('cls')
clear()

# Create DQA object
dqa = DQA()

# Set to your context document. Note that the system currently only
# supports .docx documents.
file_path = '/path/to/mydata.docx'

dqa.load_file(file_path)

# If you want to pose questions interactively, set questions to None:
questions = None # Use None for interactive

# If you want to use predefined questions, set questions:
#questions = ['What is the subject?', 'Who purchased the food?']

print("START")
print("=================================================================")

done = False
start_all = time.time()

if questions:
    print("Questions hardcoded (AUTO).\n")
    for i, question in enumerate(questions):
        print(f"Question {i}: {question}")
        start = time.time()
        results = dqa.get_answers(question, search_all=dqa.SEARCH_ALL)
        #print("***\n ")
        for result in results:
            chunk_ind = result.chunk_ref
            if dqa.SHOW_REFS == 'True':
                print(f"REF {chunk_ind}: {dqa.get_chunk(chunk_ind)}\n")
            print(f" - {result.model}: (ref: {result.chunk_ref}) {result.answer} (confidence: {result.score} )")
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
        results = dqa.get_answers(question, search_all=dqa.SEARCH_ALL)
        #print("***\n ")
        for result in results:
            chunk_ind = result.chunk_ref
            if dqa.SHOW_REFS == 'True':
                print(f"REF {chunk_ind}: {dqa.get_chunk(chunk_ind)}\n")
            print(f" - {result.model}: (ref: {result.chunk_ref}) {result.answer} (confidence: {result.score} )")
        # Show elapsed
        end = time.time()
        elapsed = end - start
        elapsed_str = time.strftime('%Hh:%Mm:%Ss', time.gmtime(elapsed))
        print(f"Elapsed: {elapsed_str}\n")

end = time.time()
elapsed_total = end - start_all
elapsed_total_str = time.strftime('%Hh:%Mm:%Ss', time.gmtime(elapsed_total))
print(f"END. Total elapsed: {elapsed_total_str}\n")
    
