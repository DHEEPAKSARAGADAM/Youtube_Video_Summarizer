import youtube_dl
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
import speech_recognition as sr
from gensim.summarization import summarize
from fpdf import FPDF

# First Downloading Youtube Video
def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# If there is no subscripts for the given URL Video
#Automatic Speech Recognition (ASR):
import speech_recognition as sr
def transcribe_audio(video_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(video_path) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio, key='YOUR_GOOGLE_API_KEY')
    return text

# Preprocessing Text by Lemmatization, Tokenization
def preprocess_text(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    return " ".join(lemmatized_words)

# Summarization
def summarize_video(video_url):
    download_video(video_url)
    transcribed_text = transcribe_audio('video.mp4')
    preprocessed_text = preprocess_text(transcribed_text)
    summary = summarize(preprocessed_text)
    return summary

# Making PDF
  def generate_pdf(summary):
      pdf = FPDF()
      pdf.add_page()
      pdf.set_font("Arial", size=12)
      pdf.multi_cell(0, 10, txt=summary)
      pdf.output("summary.pdf")
    
#Driver code
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=UF8uR6Z6KLc&t=43s"
    main(video_url)
  
  
  

