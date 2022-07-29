from itertools import count
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from courses.models import Course, Lection
from courses.forms import AddCourseModelForm

# Create your views here.
class CoursesView(View):

    def get(self, req):
        courses = Course.objects.all()
        return render(req, 'home.html', { 'courses': courses })

class AddCourseView(LoginRequiredMixin, View):
    def get(self, req):
        return render(req, 'add_course.html', {'form': AddCourseModelForm()})

    def post(self, req):
        form = AddCourseModelForm(req.POST, req.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = req.user
            course.save()
            form.save_m2m()
            return redirect('courses')
        return render(req, 'add_course.html', {'form': AddCourseModelForm()})


class LectionsView(View):

    def get(self, req, course_id):
        course = Course.objects.get(id = course_id)
        lections = Lection.objects.filter(course_id = course_id)
        return render(req, 'lections.html', { 'course': course, 'lections': lections })
