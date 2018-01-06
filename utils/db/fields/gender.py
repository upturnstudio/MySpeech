from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICE = [('f', 'female'),('m', 'male'),('n', 'none')]

class GenderField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 1)
        kwargs.setdefault('choices', GENDER_CHOICE)
        super(CharField, self).__init__(*args,**kwargs)

    def get_internal_type(self):
        return 'CharField'
