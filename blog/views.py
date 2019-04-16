from django.shortcuts import render

# Create your views here.
def poll_list(request):
    return render(request,'blog/poll_list.html',{})
