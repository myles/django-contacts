import datetime

from django.db.models import Manager, Q

class SpecialDateManager(Manager):
	
	def get_dates_for_day(self, date=None):
		"""
		Return the list of special dates for a given day.
		"""
		
		if not date:
			date = datetime.date.today()
		
		special_dates = self.get_query_set().filter(
			Q(date=date) |
			Q(every_year=True, date__month=date.month, date__day=date.day)
		)
		
		return special_dates
	
	def get_dates_for_month(self, date=None):
		"""
		Return the list of special dates for a given month.
		"""
		
		if not date:
			date = datetime.date.today()
		
		special_dates = self.get_query_set().filter(
			Q(date__month=date.month, date__year=date.year) |
			Q(every_year=True, date__month=date.month)
		)
		
		return special_dates
	
	def get_dates_for_year(self, date=None):
		"""
		Return the list of special dates for a given year.
		"""
		
		if not date:
			date = datetime.date.today()
		
		special_dates = self.get_query_set().filter(
			Q(date__year=date.year) |
			Q(every_year=True)
		)
		
		return special_dates
