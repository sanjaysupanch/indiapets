from django.shortcuts import render

# Create your views here.
def feedback(request):
    # context= { "a": "This is a context "}
    return render(request, 'feedback/feedback.html')
