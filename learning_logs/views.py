from django.shortcuts import render, redirect
from .zoom import create_zoom_meeting

from .models import Topic
from .forms import TopicForm, EntryForm

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
            return redirect('learning_logs:topics')


    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Adding new entry"""
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else: 
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topics', topic_id = topic_id)

    """display if entry is blank or invalid"""
    context = {'topic': topic,'form':form}
    return render(request, 'learning_logs/new_entry.html', context) 

def create_meeting(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        meeting_data = create_zoom_meeting(topic)
        # Process the meeting data or return it to the template
    else:
        # Render your form template
        return render(request, 'learning_logs/create_meeting.html')


