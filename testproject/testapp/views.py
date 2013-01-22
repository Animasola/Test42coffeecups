#-*- coding:utf-8 -*-
from django.views.generic.simple import direct_to_template

from testapp.models import PersonalInfo


def my_info_main(request):
    my_personal_data = PersonalInfo.objects.filter()
    resp_dict = {'my_data': my_personal_data, 'user': request.user}
    return direct_to_template(request, 'mainpage.html', resp_dict)
