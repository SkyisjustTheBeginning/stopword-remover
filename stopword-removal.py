from gensim.parsing.preprocessing import remove_stopwords
sentence = str(input("Sentence : "))
filtered_sentence = remove_stopwords(sentence)
