import gradio as gr
from google import genai
import speech_recognition as sr
from gtts import gTTS
import tempfile

client=genai.Client(api_key=" ")

#Speech to Text
def speech_to_text(audio):
  recognizer=sr.Recognizer()

  with sr.AudioFile(audio) as source:
    audio_data=recognizer.record(source)
  try:
    return recognizer.recognize_google(audio_data)
  except:
    return "Sorry, I couldn't understand."

def ask_gemini(text):
  response=client.models.generate_content(
      model="gemini-2.5-flash",
      contents=text
  )
  return response.text
