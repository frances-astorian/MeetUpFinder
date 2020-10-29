from django.test import TestCase
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Event
# Create your tests here.
class PracticeTest(TestCase):
    def testTest(self):
        self.assertTrue(True)

class test_cases(self):
	def create_event(title_text, location_text, date, time, category_text, description_text, address, geolocation):
		return Event.objects.create(title_text=question_text, location_text=location_text, date = date, time = time, category_text = category_text, description_text=description_text, address=address,geolocation=geolocation)

	def check_if_date_is_past(self):
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		create_event(title_text="Past event", location_text="location", date=-10, time = time, category_text="Food", description_text="a past event", address="The lawn")
		response = self.client.get(reverse('events:post_event'))
		self.assertQuerysetEqual(
			response.context['events_list'],
			['<Event: Past event>']
		)
	def check_no_events(self):
		response = self.client.get(reverse('events:event_list'))
		self.assertContains(response, "No events have been posted.")
		self.assertQuerysetEqual(response.context['events_list'], [])

	def check_future_events(self):
		create_event(title_text="future event", location_text = "Rotunda", date = 30, time = timezone.now(), category_text="Food", description_text="An event in the future", address=University of Virginia)
		response = self.client.get(reverse('events:event_list'))
		self.assertQuerysetEqual(
			response.context['events_list'],
			['<Event: future event>']
		)