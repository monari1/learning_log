from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

# Create your views here
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    # show all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else: 
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)


