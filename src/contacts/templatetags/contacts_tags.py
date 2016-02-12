import re

from django import template
from django.conf import settings
from django.apps import apps

Person = apps.get_model('contacts', 'person')
Company = apps.get_model('contacts', 'company')

register = template.Library()

def base_tag(parser, token, cls):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    
    m = re.search(r'(.*?) as (\w+)', arg)
    
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    
    format_string, var_name = m.groups()
    
    return cls(format_string[0], var_name)

class RecentModifiedCompanies(template.Node):
    """
    Get's a list of the recent modified companies.
    """
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name
    
    def render(self, context):
        companies = Company.objects.all().order_by("-date_modified")[:int(self.limit)]
        if (int(self.limit) == 1):
            context[self.var_name] = companies[0]
        else:
            context[self.var_name] = companies
        
        return ''

@register.tag
def get_recent_modified_companies(parser, token):
    """
    Gets any number of the recent modified comapnies.
    
    Syntax::
        
        {% get_recent_modified_companies [limit] as [var_name] %}
    """
    return base_tag(parser, token, RecentModifiedCompanies)

class RecentCreatedCompanies(template.Node):
    """
    Get's a list of the recent created companies.
    """
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name
    
    def render(self, context):
        companies = Company.objects.all().order_by("-date_added")[:int(self.limit)]
        if (int(self.limit) == 1):
            context[self.var_name] = companies[0]
        else:
            context[self.var_name] = companies
        
        return ''

@register.tag
def get_recent_added_companies(parser, token):
    """
    Gets any number of the recent added comapnies.

    Syntax::

        {% get_recent_added_companies [limit] as [var_name] %}
    """
    return base_tag(parser, token, RecentCreatedCompanies)

class RecentModifiedPeople(template.Node):
    """
    Get's a list of the recent modified people.
    """
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name

    def render(self, context):
        people = Person.objects.all().order_by("-date_modified")[:int(self.limit)]
        if (int(self.limit) == 1):
            context[self.var_name] = people[0]
        else:
            context[self.var_name] = people

        return ''

@register.tag
def get_recent_modified_people(parser, token):
    """
    Gets any number of the recent modified people.

    Syntax::

        {% get_recent_modified_people [limit] as [var_name] %}
    """
    return base_tag(parser, token, RecentModifiedPeople)

class RecentCreatedPeople(template.Node):
    """
    Get's a list of the recent created people.
    """
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name

    def render(self, context):
        people = Person.objects.all().order_by("-date_added")[:int(self.limit)]
        if (int(self.limit) == 1):
            context[self.var_name] = people[0]
        else:
            context[self.var_name] = people

        return ''

@register.tag
def get_recent_added_people(parser, token):
    """
    Gets any number of the recent added people.

    Syntax::

        {% get_recent_added_people [limit] as [var_name] %}
    """
    return base_tag(parser, token, RecentCreatedPeople)