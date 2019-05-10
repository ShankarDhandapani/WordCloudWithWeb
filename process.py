from flask import Flask
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
#@app.route('/hello')
#def hello_world():
#    return 'Hello World!'

@app.route('/<username>')
def hello_world(username):
    names = username;
    stopwords = set(STOPWORDS)
    # instantiate a word cloud object
    wc = WordCloud(
        background_color='white',
        max_words=2000,
        stopwords=stopwords
        )
    # generate the word cloud
    wc.generate(str(names))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    return ''

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5004)
