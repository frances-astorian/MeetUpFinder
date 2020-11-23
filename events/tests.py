from django.test import TestCase
import datetime

from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Event, Category
# Create your tests here.

def create_category(name):
	return Category.objects.create(name = name)
def create_organizer(organizer):
	return Event.objects.create(organizer = organizer)
def create_title(organizer, title_text):
	return Event.objects.create(organizer = organizer, title_text = title_text)
def create_location(organizer, title_text, location_text):
	return Event.objects.create(organizer = organizer, title_text = title_text, location_text = location_text)
def create_date(organizer, title_text, location_text, date):
	return Event.objects.create(organizer = organizer, title_text = title_text, location_text = location_text, date = date)
def create_time(organizer, title_text, location_text, date, time):
	return Event.objects.create(organizer = organizer, title_text = title_text, location_text = location_text, date = date, time = time)
def create_category_text(organizer, title_text, location_text, date, time, category_text):
	return Event.objects.create(organizer = organizer, title_text = title_text, location_text = location_text, date = date, time = time, category_text= category_text)
def create_description_text(organizer, title_text, location_text, date, time, category_text, description_text):
	return Event.objects.create(organizer = organizer, title_text = title_text, location_text = location_text, date = date, time = time, category_text= category_text, description_text=description_text)


class CategoryCases(TestCase):
	def test_create(self):
		e1 = create_category(name = "test")
		self.assertEqual(e1, Category.objects.get(name="test"))
		# return Event.objects.create(title = "test")
class EventCases(TestCase):
	def test_create_organizer(self):
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		e1 = create_organizer(organizer=user)
		self.assertEqual(e1, Event.objects.get(organizer=user))
	def test_create_title(self):
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		e1  = create_title(organizer = user, title_text = "A new_test")
		self.assertEqual(e1, Event.objects.get(organizer = user, title_text= "A new_test"))
	def test_location_text(self):
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		e1  = create_location(organizer = user, title_text = "A new_test2", location_text="Corner Grocery")
		self.assertEqual(e1, Event.objects.get(organizer = user, title_text = "A new_test2", location_text="Corner Grocery"))
	def test_date(self):
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		e1  = create_date(organizer = user, title_text = "A new_test", location_text="Corner Grocery", date = "2020-11-17")
		self.assertEqual(e1, Event.objects.get(organizer = user, title_text = "A new_test", location_text="Corner Grocery", date = "2020-11-17"))
	def test_time(self):
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		e1  = create_time(organizer = user, title_text = "A new_test", location_text="Corner Grocery", date = "2020-11-17", time = "14:30")
		self.assertEqual(e1, Event.objects.get(organizer = user, title_text = "A new_test", location_text="Corner Grocery", date = "2020-11-17", time = "14:30"))
	def test_category(self):
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		e1  = create_category_text(organizer = user, title_text = "A new_test", location_text="Corner Grocery", date = "2020-11-17", time = "14:30", category_text= "Food")
		self.assertEqual(e1, Event.objects.get(organizer = user, title_text = "A new_test", location_text="Corner Grocery", date = "2020-11-17", time = "14:30", category_text= "Food"))
	def test_description(self):
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		e1  = create_description_text(organizer = user, title_text = "A new_test", location_text="Corner Grocery", date = "2020-11-17", time = "14:30", category_text= "Food", description_text="a description")
		self.assertEqual(e1, Event.objects.get(organizer = user, title_text = "A new_test", location_text="Corner Grocery", date = "2020-11-17", time = "14:30", category_text= "Food", description_text="a description"))
	
	def test_check_if_date_is_past(self):
		user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		e1 = create_time(organizer = user, title_text="Past event", location_text="Corner Grocery", date = "2020-11-17", time = "14:30" )
		e1.save()
		response = self.client.get(reverse('events:event_list'))
		self.assertQuerysetEqual(response.context['events_list'],[])

	def test_check_no_events(self):
		response = self.client.get(reverse('events:event_list'))
		self.assertQuerysetEqual(response.context['events_list'], [])
		# self.assertContains(response, "No events have been posted.")

	# def test_check_future_events(self):
	# 	user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
	# 	time = timezone.now() + datetime.timedelta(hours=23, minutes=59, seconds=59)
	# 	e1 = create_title(organizer = user, title_text="Past event")
	# 	response = self.client.get(reverse('events:event_list'))
	# 	self.assertQuerysetEqual(response.context['events_list'],['<Event: future event>'])

class authentication_tests(TestCase):
	def test_events(self):
		response = self.client.get('/events/')
		self.assertEqual(response.status_code, 200)
	def test_events_list(self):
		response = self.client.get('/events/list/')
		self.assertEqual(response.status_code, 200)
	def test_category_food(self):
		response = self.client.get('/events/category/Food/')
		self.assertEqual(response.status_code, 200) 
	def test_category_phys_Activity(self):
		response = self.client.get('/events/category/Physical%20Activity/')
		self.assertEqual(response.status_code, 200)
	def test_category_civ_engagement(self):
		response = self.client.get('/events/category/Civic%20Engagement/')
		self.assertEqual(response.status_code, 200)
	def test_category_entertainment(self):
		response = self.client.get('/events/category/Entertainment/')
		self.assertEqual(response.status_code, 200)
	def test_nonexistent_profile(self):
		response = self.client.get('/social/2/profile/')
		self.assertEqual(response.status_code, 404)
	def test_nonexistent_your_events(self):
		response = self.client.get('/your-events/')
		self.assertEqual(response.status_code, 404)
	def test_search_for_users(self):
		response = self.client.get('/social/search_users/')
		self.assertEqual(response.status_code, 200)
	def test_none(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

