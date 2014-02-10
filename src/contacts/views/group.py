from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404, HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from contacts.models import Group
from contacts.forms import GroupCreateForm, GroupUpdateForm

def list(request, page=1, template='contacts/group/list.html'):
    """List of all the groups.

    :param template: Add a custom template.
    """

    group_list = Group.objects.all()
    paginator = Paginator(group_list, 20)

    try:
        groups = paginator.page(page)
    except (EmptyPage, InvalidPage):
        groups = paginator.page(paginator.num_pages)

    kwvars = {
        'object_list': groups.object_list,
        'has_next': groups.has_next(),
        'has_previous': groups.has_previous(),
        'has_other_pages': groups.has_other_pages(),
        'start_index': groups.start_index(),
        'end_index': groups.end_index(),
    }

    try:
        kwvars['previous_page_number'] = groups.previous_page_number()
    except (EmptyPage, InvalidPage):
        kwvars['previous_page_number'] = None
    try:
        kwvars['next_page_number'] = groups.next_page_number()
    except (EmptyPage, InvalidPage):
        kwvars['next_page_number'] = None

    return render_to_response(template, kwvars, RequestContext(request))

def detail(request, pk, slug=None, template='contacts/group/detail.html'):
    """Detail of a group.

    :param template: Add a custom template.
    """

    try:
        group = Group.objects.get(pk__iexact=pk)
    except Group.DoesNotExist:
        raise Http404

    kwvars = {
        'object': group,
    }

    return render_to_response(template, kwvars, RequestContext(request))

def create(request, template='contacts/group/create.html'):
    """Create a group.

    :param template: A custom template.
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

    kwvars = {
        'form': GroupCreateForm(request.POST)
    }

    return render_to_response(template, kwvars, RequestContext(request))

def update(request, pk, slug=None, template='contacts/group/update.html'):
    """Update a group.

    :param template: A custom template.
    :param form: A custom form.
    """

    user = request.user
    if not user.has_perm('change_group'):
        return HttpResponseForbidden()

    try:
        group = Group.objects.get(pk__iexact=pk)
    except Group.DoesNotExist:
        raise Http404

    form = GroupUpdateForm(instance=group)

    if request.method == 'POST':
        form = GroupUpdateForm(request.POST, instance=group)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(group.get_absolute_url())

    kwvars = {
        'form': form,
        'object': group,
    }

    return render_to_response(template, kwvars, RequestContext(request))

def delete(request, pk, slug=None, template='contacts/group/delete.html'):
    """Update a group.

    :param template: A custom template.
    """

    user = request.user
    if not user.has_perm('delete_group'):
        return HttpResponseForbidden()

    try:
        group = Group.objects.get(pk__iexact=pk)
    except Group.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        new_data = request.POST.copy()
        if new_data['delete_group'] == 'Yes':
            group.delete()
            return HttpResponseRedirect(reverse('contacts_group_list'))
        else:
            return HttpResponseRedirect(group.get_absolute_url())

    kwvars = {
        'object': group,
    }

    return render_to_response(template, kwvars, RequestContext(request))