from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404, HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect

from contacts.models import Company, Person
from contacts.forms import *

def company_list(request, page=1, template_name='contacts/company/list.html'):
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

def company_detail(request, slug, template_name='contacts/company/detail.html'):
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

def company_create(request, template_name='contacts/company/create.html'):
	"""Create a company.
	
	:param template_name: A custom template.
	:param form: A custom form.
	"""
	
	user = request.user
	if not user.has_perm('add_company'):
		return HttpResponseForbidden()
	
	if request.method == 'POST':
		company_form = CompanyCreateForm(request.POST)
		if company_form.is_valid():
			c = company_form.save(commit=False)
			
			# TODO Make sure that the slug isn't already in the database
			if c.nickname:
				c.slug = slugify(c.nickname)
			else:
				c.slug = slugify(c.name)
			
			c.save()
			return HttpResponseRedirect(c.get_absolute_url())
		else:
			return HttpResponseServerError
	
	context = {
		'form': CompanyCreateForm(request.POST)
	}
	
	return render_to_response(template_name, context,
		context_instance=RequestContext(request))

def company_update(request, slug, template_name='contacts/company/update.html'):
	"""Update a company.
	
	:param template_name: A custom template.
	:param form: A custom form.
	"""
	
	user = request.user
	if not user.has_perm('change_company'):
		return HttpResponseForbidden()
	
	try:
		company = Company.objects.get(slug__iexact=slug)
	except Company.DoesNotExist:
		raise Http404
	
	if request.method == 'POST':
		form = CompanyUpdateForm(request.POST, instance=company)
		phone_formset = PhoneNumberFormSet(request.POST, instance=company)
		email_formset = EmailAddressFormSet(request,POST, instance=company)
		im_formset = InstantMessengerFormSet(request.POST, instance=company)
		website_formset = WebSiteFormSet(request.POST, instance=company)
		address_formset = StreetAddressFormSet(request.POST, instance=company)
		
		if form.is_valid() and phone_formset.is_valid() and \
			email_formset.is_valid() and im_formset.is_valid() and \
			website_formset.is_valid() and address_formset.is_valid():
			form.save()
			phone_formset.save()
			email_formset.save()
			im_formset.save()
			website_formset.save()
			address_formset.save()
			return HttpResponseRedirect(company.get_absolute_url())
		else:
			return HttpResponseServerError
	
	form = CompanyUpdateForm(instance=company)
	phone_formset = PhoneNumberFormSet(instance=company)
	email_formset = EmailAddressFormSet(instance=company)
	im_formset = InstantMessengerFormSet(instance=company)
	website_formset = WebSiteFormSet(instance=company)
	address_formset = StreetAddressFormSet(instance=company)
	
	context = {
		'form': form,
		'phone_formset': phone_formset,
		'email_formset': email_formset,
		'im_formset': im_formset,
		'website_formset': website_formset,
		'address_formset': address_formset,
		'object': company,
	}
	
	return render_to_response(template_name, context,
		context_instance=RequestContext(request))

def company_delete(request, slug, template_name='contacts/company/delete.html'):
	"""Update a company.
	
	:param template_name: A custom template.
	"""
	
	user = request.user
	if not user.has_perm('delete_company'):
		return HttpResponseForbidden()
	
	try:
		company = Company.objects.get(slug__iexact=slug)
	except Company.DoesNotExist:
		raise Http404
	
	if request.method == 'POST':
		new_data = request.POST.copy()
		if new_data['delete_company'] == 'Yes':
			company.delete()
			return HttpResponseRedirect(reverse('contacts_company_list'))
		else:
			return HttpResponseRedirect(company.get_absolute_url())
	
	context = {
		'object': company,
	}
	
	return render_to_response(template_name, context,
		context_instance=RequestContext(request))

def person_list(request, page=1, template_name='contacts/person/list.html'):
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

def person_detail(request, slug, template_name='contacts/person/detail.html'):
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

def person_create(request, template_name='contacts/person/create.html'):
	"""Create a person.
	
	:param template_name: A custom template.
	"""

	user = request.user
	if not user.has_perm('add_person'):
		return HttpResponseForbidden()

	if request.method == 'POST':
		form = PersonCreateForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			p.slug = slugify("%s %s" % (p.first_name, p.last_name))
			p.save()
			return HttpResponseRedirect(p.get_absolute_url())
		else:
			return HttpResponseServerError

	context = {
		'form': PersonCreateForm(request.POST)
	}

	return render_to_response(template_name, context,
		context_instance=RequestContext(request))

def person_update(request, slug, template_name='contacts/person/update.html'):
	"""Update a person.

	:param template_name: A custom template.
	"""

	user = request.user
	if not user.has_perm('change_person'):
		return HttpResponseForbidden()

	try:
		person = Person.objects.get(slug__iexact=slug)
	except person.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = PersonUpdateForm(request.POST, instance=person)
		phone_formset = PhoneNumberFormSet(request.POST, instance=person)
		email_formset = EmailAddressFormSet(request.POST, instance=person)
		im_formset = InstantMessengerFormSet(request.POST, instance=person)
		website_formset = WebSiteFormSet(request.POST, instance=person)
		address_formset = StreetAddressFormSet(request.POST, instance=person)

		if form.is_valid() and phone_formset.is_valid() and \
			email_formset.is_valid() and im_formset.is_valid() and \
			website_formset.is_valid() and address_formset.is_valid():
			form.save()
			phone_formset.save()
			email_formset.save()
			im_formset.save()
			website_formset.save()
			address_formset.save()
			return HttpResponseRedirect(person.get_absolute_url())
		else:
			return HttpResponseServerError

	form = PersonUpdateForm(instance=person)
	phone_formset = PhoneNumberFormSet(instance=person)
	email_formset = EmailAddressFormSet(instance=person)
	im_formset = InstantMessengerFormSet(instance=person)
	website_formset = WebSiteFormSet(instance=person)
	address_formset = StreetAddressFormSet(instance=person)

	context = {
		'form': form,
		'phone_formset': phone_formset,
		'email_formset': email_formset,
		'im_formset': im_formset,
		'website_formset': website_formset,
		'address_formset': address_formset,
		'object': person,
	}

	return render_to_response(template_name, context,
		context_instance=RequestContext(request))

def person_delete(request, slug, template_name='contacts/person/delete.html'):
	"""Delete a company.

	:param template_name: A custom template.
	"""

	user = request.user
	if not user.has_perm('delete_person'):
		return HttpResponseForbidden()

	try:
		person = Person.objects.get(slug__iexact=slug)
	except Person.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		new_data = request.POST.copy()
		if new_data['delete_person'] == 'Yes':
			person.delete()
			return HttpResponseRedirect(reverse('contacts_person_list'))
		else:
			return HttpResponseRedirect(person.get_absolute_url())

	context = {
		'object': person,
	}

	return render_to_response(template_name, context,
		context_instance=RequestContext(request))
