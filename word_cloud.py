from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pandas as pd
import re
import string

def word_cloud(project_path, csv_file_path_and_file_name):
    
    # Read the file
    df = pd.read_csv(project_path+csv_file_path_and_file_name, encoding="latin-1", error_bad_lines=False)
    text = df.values
    comment_words = ''
    stopwords = set(STOPWORDS)
    
    result = []

    for val in text:
        val = str(val)
        tokens = val.split()
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        new_tokens = []
        
             
        for i in range(len(tokens)):         
          if (tokens[i] not in stopwords):
              tokens[i] = re.sub(r'\d+', '', tokens[i])
              tokens[i] = tokens[i].translate(str.maketrans('','', string.punctuation)) 
              if 'https' not in tokens[i]:                
                  new_tokens.append(tokens[i])
          result.append(new_tokens)
          print(new_tokens)
          comment_words += " ".join(new_tokens) + " "

    
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()
    
    
if __name__ == '__main__':
    # folder address
    project_path = "D:\\....................................."
    # file name and its format (e.g. Data.csv)
    csv_file_path_and_file_name = "\\----------------------.csv"
    word_cloud(project_path, csv_file_path_and_file_name)
