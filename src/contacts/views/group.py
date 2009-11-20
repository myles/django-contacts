from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404, HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect

from contacts.models import Group
from contacts.views import small_render_to_response
from contacts.forms import GroupCreateForm, GroupUpdateForm