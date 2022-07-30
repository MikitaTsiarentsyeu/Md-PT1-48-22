from django.contrib import admin
from django.http import HttpResponseRedirect
from .forms import ProductForm
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'brend', 'cross', 'quantity', 'cost', 'parsing_date')
#    list_filter = ('article')
    form = ProductForm

    change_form_template = "admin/change_form.html"


    def response_change(self, request, obj):
        if "_make-unique" in request.POST:
#            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
 #           matching_names_except_this.delete()
            obj.is_unique = True
            obj.save()
            self.message_user(request)
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)