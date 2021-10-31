from django.shortcuts import render
from googletrans import Translator

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        text=request.POST.get("pretext")
        f = request.POST.get("from")
        t = request.POST.get('to')
        translator = Translator()
        trans = translator.translate(text, src=f, dest=t)
       
        context.update({
            "text":trans.text,
            "pretext" : text,
            "from": f,
            "to": t
        })
    return render(request, 'trans/index.html',context)

