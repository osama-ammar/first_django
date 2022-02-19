from django.shortcuts import render

def post_list(request):
    return render(request, 'radiosh/post_list.html', {})