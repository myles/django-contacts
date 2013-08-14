import datetime

from django.db.models import Manager, Q

class SpecialDateManager(Manager):
	
	def get_dates(self, date=None):
		"""
		Return a list of special dates for a given day even if the date is
		recurring every year.
		"""
		
		if not date:
			date = datetime.date.today()
		
		special_dates = self.get_query_set().filter(
			Q(date=date) |
			Q(every_year=True, date__month=date.month, date__day=date.day)
		)
		
		return special_dates