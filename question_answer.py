from transformers import pipeline

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


def is_valid(answer):
    if not answer:
        return False
    elif "<s>" in answer or "</s>" in answer:
        return False
    else:
        return True


class Result:
    def __init__(self, model, answer, score):
        self.model = model
        self.answer = answer
        self.score = score


def get_answers(question, docs):
    answers = []
    max_false_positive = 0.00000000000000000001
    for i, doc in enumerate(docs):
        #print(f"Examining: {i}")
        result = model_0(question=question, context=doc)
        if is_valid(result.get("answer")):
            r = Result('model_0', result.get("answer"), result.get("score"))
            if not any(r.answer == x.answer for x in answers):
                answers.append(r)
            else:
                r = Result('model_0', '-----------------', max_false_positive)
                answers.append(r)
      
        result = model_1(question=question, context=doc)
        if is_valid(result.get("answer")):
            r = Result('model_1', result.get("answer"), result.get("score"))
            if not any(r.answer == x.answer for x in answers):
                answers.append(r)
            else:
                r = Result('model_1', '-----------------', max_false_positive)
                answers.append(r)
       
        result = model_2(question=question, context=doc)
        if is_valid(result.get("answer")):
            r = Result('model_2', result.get("answer"), result.get("score"))
            if not any(r.answer == x.answer for x in answers):
                answers.append(r)
            else:
                r = Result('model_2', '-----------------', max_false_positive)
                answers.append(r)

        result = model_3(question=question, context=doc)
        if is_valid(result.get("answer")):
            r = Result('model_3', result.get("answer"), result.get("score"))
            if not any(r.answer == x.answer for x in answers):
                answers.append(r)
            else:
                r = Result('model_3', '-----------------', max_false_positive)
                answers.append(r)

        result = model_4(question=question, context=doc)
        if is_valid(result.get("answer")):
            r = Result('model_4', result.get("answer"), result.get("score"))
            if not any(r.answer == x.answer for x in answers):
                answers.append(r)
            else:
                r = Result('model_4', '-----------------', max_false_positive)
                answers.append(r)

        result = model_5(question=question, context=doc)
        if is_valid(result.get("answer")):
            r = Result('model_5', result.get("answer"), result.get("score"))
            if not any(r.answer == x.answer for x in answers):
                answers.append(r)
            else:
                r = Result('model_5', '-----------------', max_false_positive)
                answers.append(r)       

    # To return a new list, use the sorted() built-in function...
    answers.sort(key=lambda x: x.score, reverse=True)
    return answers
