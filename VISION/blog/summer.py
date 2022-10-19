import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx # NetworkX is a package for the Python programming language that's used to create, manipulate, and study the structure, dynamics, and functions of complex graph networks

def read_article(file_name):
    sentences = []
    # file = open(file_name, 'r') 
    # f_data = file.readlines()
    # f_data = [x for x in f_data if x != '\n'] # it should remove any break present
    # f_data = [x.replace('\n',' ') for x in f_data] #this would remove that end of line
    # f_data = ''.join(f_data) 
    article = file_name.split('. ') 
    for sentence in article:
        sentences.append(sentence.replace("^[a-zA-Z0-9!@#$&()-`+,/\"]", " ").split(" "))
    return sentences
"""### Define a Cosine Similarity matrix"""

def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))  # Create an empty similarity matrix
    
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: # ignore if both are same sentences
                continue 
                similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
    return similarity_matrix

"""### We start our Algo step by step"""

def generate_summary(file_name, top_n=4):
    
    # nltk.download("stopwords")    ### if not already installed, delete the # and run the code one time
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 1 - Input Article and split it into Sentences
    sentences =  read_article(file_name)

    # Step 2 - Build a Similary Martix across sentences & remove Stop Words
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Generate rank based on Matrix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    # print("Indexes of top ranked_sentence order are ", ranked_sentence)    

    for i in range(top_n):
      summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - output the summarized text
    return(summarize_text)
