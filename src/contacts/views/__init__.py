from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.defaultfilters import slugify

def small_render_to_response(request, template_name, context):
	"""A small 'render_to_response'.
	
	:param request:
	:param template_name:
	:param context:
	"""
	
	return render_to_response(template_name, context,
		context_instance=RequestContext(request))