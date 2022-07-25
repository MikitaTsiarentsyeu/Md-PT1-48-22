from django.shortcuts import render
from django.views import View

from courses.models import Course, Lection

# Create your views here.
class CoursesView(View):

    def get(self, req):
        courses = Course.objects.all()
        return render(req, 'home.html', { 'courses': courses })

class LectionsView(View):

    def get(self, req, course_id):
        lections = Lection.objects.filter(course_id = course_id)
        return render(req, 'lections.html', { 'lections': lections })
