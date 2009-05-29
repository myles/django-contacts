from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from contacts.models import Company, Person

def company_list(request, page=1, template_name='contacts/company_list.html'):
	"""List of all the comapnies.
	
	:param template_name: Add a custom template.
	"""
	company_list = Company.objects.all()
	paginator = Paginator(company_list, 20)
	
	try:
		companies = paginator.page(page)
	except (EmptyPage, InvalidPage):
		companies = paginator.page(paginator.num_pages)
	
	context = {
		'object_list': companies.object_list,
		'has_next': companies.has_next(),
		'has_previous': companies.has_previous(),
		'has_other_pages': companies.has_other_pages(),
		'start_index': companies.start_index(),
		'end_index': companies.end_index(),
		'previous_page_number': companies.previous_page_number(),
		'next_page_number': companies.next_page_number(),
	}
	
	return render_to_response(template_name, context,
		context_instance=RequestContext(request))

def company_detail(request, slug, template_name='contacts/company_detail.html'):
	"""Detail of a company.

	:param template_name: Add a custom template.
	"""

	try:
		company = Company.objects.get(slug__iexact=slug)
	except Company.DoesNotExist:
		raise Http404

	context = {
		'object': company,
	}

	return render_to_response(template_name, context,
		context_instance=RequestContext(request))

def person_list(request, page=1, template_name='contacts/person_list.html'):
	"""List of all the people.
	
	:param template_name: Add a custom template.
	"""
	
	person_list = Person.objects.all()
	paginator = Paginator(person_list, 20)
	
	try:
		people = paginator.page(page)
	except (EmptyPage, InvalidPage):
		people = paginator.page(paginator.num_pages)
	
	context = {
		'object_list': people.object_list,
		'has_next': people.has_next(),
		'has_previous': people.has_previous(),
		'has_other_pages': people.has_other_pages(),
		'start_index': people.start_index(),
		'end_index': people.end_index(),
		'previous_page_number': people.previous_page_number(),
		'next_page_number': people.next_page_number(),
	}
	
	return render_to_response(template_name, context,
		context_instance=RequestContext(request))

def person_detail(request, slug, template_name='contacts/person_detail.html'):
	"""Detail of a person.
	
	:param template_name: Add a custom template.
	"""
	
	try:
		person = Person.objects.get(slug__iexact=slug)
	except Person.DoesNotExist:
		raise Http404
	
	context = {
		'object': person,
	}
	
	return render_to_response(template_name, context,
		context_instance=RequestContext(request))