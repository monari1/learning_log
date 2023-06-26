import zoomus
from django.conf import settings

def create_zoom_meeting(topic):
    client = zoomus.ZoomClient(settings.ZOOM_API_KEY, settings.ZOOM_API_SECRET)
    response = client.meeting.create(user_id='me', topic=topic)
    return response.json()
