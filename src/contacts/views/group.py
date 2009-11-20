from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404, HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect

from contacts.models import Group
from contacts.views import small_render_to_response
from contacts.forms import GroupCreateForm, GroupUpdateForm

def list(request, page=1, template_name='contacts/group/list.html'):
	"""List of all the groups.
	
	:param template_name: Add a custom template.
	"""
	group_list = Group.objects.all()
	paginator = Paginator(group_list, 20)
	
	try:
		groups = paginator.page(page)
	except (EmptyPage, InvalidPage):
		groups = paginator.page(paginator.num_pages)
	
	context = {
		'object_list': groups.object_list,
		'has_next': groups.has_next(),
		'has_previous': groups.has_previous(),
		'has_other_pages': groups.has_other_pages(),
		'start_index': groups.start_index(),
		'end_index': groups.end_index(),
		'previous_page_number': groups.previous_page_number(),
		'next_page_number': groups.next_page_number(),
	}
	
	return small_render_to_response(request, template_name, context)

def detail(request, slug, template_name='contacts/group/detail.html'):
	"""Detail of a group.

	:param template_name: Add a custom template.
	"""
	
	try:
		group = Group.objects.get(slug__iexact=slug)
	except Group.DoesNotExist:
		raise Http404
	
	context = {
		'object': group,
	}
	
	return small_render_to_response(request, template_name, context)

def create(request, template_name='contacts/group/create.html'):
	"""Create a group.

	:param template_name: A custom template.
	:param form: A custom form.
	"""

	user = request.user
	if not user.has_perm('add_group'):
		return HttpResponseForbidden()

	if request.method == 'POST':
		group_form = GroupCreateForm(request.POST)
		if group_form.is_valid():
			g = group_form.save(commit=False)
			
			# TODO Make sure that the slug isn't already in the database
			g.slug = slugify(g.name)
			
			g.save()
			return HttpResponseRedirect(g.get_absolute_url())
		else:
			return HttpResponseServerError

	context = {
		'form': GroupCreateForm(request.POST)
	}

	return small_render_to_response(request, template_name, context)

def update(request, slug, template_name='contacts/group/update.html'):
	"""Update a group.

	:param template_name: A custom template.
	:param form: A custom form.
	"""
	
	user = request.user
	if not user.has_perm('change_group'):
		return HttpResponseForbidden()
	
	try:
		group = Group.objects.get(slug__iexact=slug)
	except Group.DoesNotExist:
		raise Http404
	
	form = GroupUpdateForm(instance=group)
	
	if request.method == 'POST':
		form = GroupUpdateForm(request.POST, instance=group)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(group.get_absolute_url())
	
	context = {
		'form': form,
		'object': group,
	}
	
	return small_render_to_response(request, template_name, context)

def delete(request, slug, template_name='contacts/group/delete.html'):
	"""Update a group.

	:param template_name: A custom template.
	"""

	user = request.user
	if not user.has_perm('delete_group'):
		return HttpResponseForbidden()

	try:
		group = Group.objects.get(slug__iexact=slug)
	except Group.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		new_data = request.POST.copy()
		if new_data['delete_group'] == 'Yes':
			group.delete()
			return HttpResponseRedirect(reverse('contacts_group_list'))
		else:
			return HttpResponseRedirect(group.get_absolute_url())

	context = {
		'object': group,
	}

	return small_render_to_response(request, template_name, context)