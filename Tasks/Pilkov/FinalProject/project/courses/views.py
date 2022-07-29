from django.views import View
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

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
    
class SignUp(View):

    def is_user_exists(*args, **kwargs):
        try:
            User.objects.get(**kwargs)
        except ObjectDoesNotExist:
            '''expected error (user not exist)'''
            return False
        else:
            return True
        

    def get(self, req):
        return render(req, 'registration/signup.html')
    
    def post(self, req):
        user = None
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')

        if self.is_user_exists(username = username) or self.is_user_exists(email = email):
            return render(req, 'registration/signup.html', {'errors':['user already exist']})

        user = User(username = username, email = email)
        user.set_password(user.password)
        user.save()

        user = authenticate(req, username=username, password=password)
        login(req, user)
        return redirect('/')