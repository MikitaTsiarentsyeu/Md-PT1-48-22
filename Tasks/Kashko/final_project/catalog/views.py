from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from catalog.forms import AddContact, AddItem
from catalog.models import Category, City, Contact, Item


def index(request):
    return render(request, 'catalog/index.html')


def help(request):
    return render(request, 'catalog/help.html')


def items(request, **kwargs):
    if (query := request.GET.get('q')):
        items_set = Item.objects.filter(
            name__icontains=query).order_by('-create_date')
    else:
        items_set = Item.objects.filter(**kwargs).order_by('-create_date')

    # Pagination
    if (per_page := request.GET.get('per_page')):
        request.session['per_page'] = int(per_page)
    per_page = request.session.get('per_page', 12)
    paginator = Paginator(items_set, per_page, orphans=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Context
    context = {
        'items_set': items_set,
        'page_obj': page_obj,
        'per_page': per_page,
        'q': query
    }

    # Context for breadcrumb
    for k, v in kwargs.items():
        if k == 'type':
            context[k] = next(filter(lambda x: v in x, Item.ITEM_TYPES))
        elif k == 'category_id':
            context['category'] = (
                v,
                Category.objects.get(id=v).name,
            )
        elif k == 'city_id':
            context['city'] = (
                v,
                City.objects.get(id=v).name,
            )

    return render(request, 'catalog/items.html', context)


def item(request, item_id):
    item = Item.objects.filter(id=item_id)[0]
    context = {'item': item}
    return render(request, 'catalog/item.html', context)


def add_item(request):
    if request.method == 'POST':

        if 'cancel' in request.POST:
            return redirect('home')

        contact_form = AddContact(request.POST, request.FILES)
        item_form = AddItem(request.POST, request.FILES)

        if all((contact_form.is_valid(), item_form.is_valid())):

            new_contact = contact_form.save(commit=False)

            contact, created = Contact.objects.update_or_create(
                email__iexact=new_contact.email,
                defaults={
                    'first_name': new_contact.first_name,
                    'last_name': new_contact.last_name,
                    'email': new_contact.email,
                    'phone_number': new_contact.phone_number
                })

            item = item_form.save(commit=False)
            if item.type == 'f':
                item.who_found = contact
            elif item.type == 'l':
                item.who_lost = contact
            item.save()
            item.refresh_from_db()

            return redirect('item', item.id)
    else:

        contact_form = AddContact()
        item_form = AddItem()

    return render(request, 'catalog/add_item.html', {
        'contact_form': contact_form,
        'item_form': item_form
    })


def respond(request, item_id):
    if request.method == 'POST':

        if 'cancel' in request.POST:
            return redirect('home')

        contact_form = AddContact(request.POST)

        if contact_form.is_valid():

            new_contact = contact_form.save(commit=False)

            contact, created = Contact.objects.update_or_create(
                email__iexact=new_contact.email,
                defaults={
                    'first_name': new_contact.first_name,
                    'last_name': new_contact.last_name,
                    'email': new_contact.email,
                    'phone_number': new_contact.phone_number
                })

            item = Item.objects.get(id=item_id)
            if item.type == 'l':
                item.who_found = contact
            elif item.type == 'f':
                item.who_lost = contact
            item.is_active = False
            item.save()
            item.refresh_from_db()

            return redirect('item', item.id)
    else:

        contact_form = AddContact()

    return render(request, 'catalog/respond.html', {
        'contact_form': contact_form
    })
