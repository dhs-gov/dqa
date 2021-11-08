import nltk

MAX_TOKENS_CHUNK = 300

def get_chunks(text):
    chunks = []
    chunk = ""
    current_length = 0
    sentences = nltk.tokenize.sent_tokenize(text)
    for sentence in sentences:
        #print(f"Adding sentence: {sentence}")
        current_length += len(sentence)
        chunk = chunk + sentence
        if current_length > MAX_TOKENS_CHUNK:
            chunks.append(chunk)
            chunk = ""
            current_length = 0

    # Append remaining chunk
    chunks.append(chunk)

    return chunks