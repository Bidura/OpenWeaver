from django.shortcuts import render
from all_images.models import Myimages
import openai
from datetime import date

openai.api_key = "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"
def dall_e_api(dalle_prompt):
    
    dalle_response = openai.Image.create(
            prompt = dalle_prompt,
            size="512x512"
        )
    image_url = dalle_response['data'][0]['url']
    
    return image_url

def whisper_transcribe(audio):
   
   transcript = openai.Audio.transcribe("whisper-1", audio)
   return transcript["text"]

def all_images(request):
  if request.method == 'POST':
    audio = request.FILES.get('mywav')
    text = whisper_transcribe(audio)
    img = dall_e_api(text) 
    images = Myimages(text=text,imgurl=img,date=date.today())
    images.save()
    return render(request,"home.html",{'img':img,'msg':'Your image has been generated and saved!','msg2':text})
  else:
    return render(request,"home.html")

# Create your views here.
#we must call the view via a URL.