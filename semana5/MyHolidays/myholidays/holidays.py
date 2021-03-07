from datetime import datetime, date
from dateutil.parser import parse
import holidays

class MyCalendar:
	def __init__(self, *args):
		self.datas = []
		for dt in args:
			obj = self.check_instance(dt)
			if obj:
				self.datas.append(obj)

	def check_instance(self, item):
		if isinstance(item, str):
			return self.normalize_date(item)
		if isinstance(item, date):
			return item
		if isinstance(item, datetime):
			return item			
		if isinstance(item, int):
			return None

	def add_holiday(self, *args):
		for e in args:
			self.datas.append(self.check_instance(e))
		self.datas = self.remove_duplicade(self.datas)

	def check_holiday(self, *args):
		countries_holidays = holidays.CA(years=2021)
		countries_holidays += holidays.USA(years=2021)
		countries_holidays += holidays.BR(years=2021)
		countries_holidays += holidays.MW(years=2021)
		for e in args:
			dt = self.check_instance(e)
			if not dt:
				return False
			feriado = dt in countries_holidays
			return feriado


	def remove_duplicade(self, datas):
		nova_lista = list(filter(lambda x : x != None, set(datas)))
		return nova_lista
	
	def normalize_date(self, dt):
		try:
			dt_f = parse(dt).date()
			return dt_f
		except:
			dt_f = None
		return dt_f
