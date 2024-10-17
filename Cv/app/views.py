from django.shortcuts import render, get_object_or_404

from .models import Customer, blogs, CategoryWeblog, OtherExample


# Create your views here.

def index(request):
    latest_blogs = blogs.objects.all()[:4]

    context = {
        'latest_blogs': latest_blogs
    }
    return render(request, 'index.html', context)


def weblogs(request):
    filter_type = request.GET.get('filter', 'popular')
    search_query = request.GET.get('search', '')

    category_slug = request.GET.get('category')

    if search_query:
        weblogs = blogs.objects.filter(title__icontains=search_query)
    else:
        if category_slug:  # اگر دسته‌بندی مشخص شده باشد
            weblogs = blogs.objects.filter(category__slug=category_slug)
        else:
            if filter_type == 'latest':
                weblogs = blogs.objects.order_by('-created_at')
            elif filter_type == 'oldest':
                weblogs = blogs.objects.order_by('created_at')
            elif filter_type == 'popular':
                weblogs = blogs.objects.order_by('-popularity')
            else:
                weblogs = blogs.objects.all()

    categories = CategoryWeblog.objects.all()[:5]

    new_blogs = blogs.objects.order_by('-created_at')[:5]
    old_blogs = blogs.objects.order_by('created_at')[:5]
    popular_blogs = blogs.objects.order_by('-popularity')[:5]

    return render(request, 'blogs.html', {
        'weblogs': weblogs,
        'categories': categories,
        'new_blogs': new_blogs,
        'old_blogs': old_blogs,
        'popular_blogs': popular_blogs,
        'search_query': search_query
    })


def blog_detail(request, id):
    blog = get_object_or_404(blogs, id=id)
    categories = CategoryWeblog.objects.all()

    new_blogs = blogs.objects.order_by('-created_at')[:5]  # نمایش ۵ نوشته جدیدترین
    old_blogs = blogs.objects.order_by('created_at')[:5]  # نمایش ۵ نوشته قدیمی‌ترین
    popular_blogs = blogs.objects.order_by('-popularity')[:5]  # نمایش ۵ نوشته محبوب ترین

    return render(request, 'blogPage.html', {
        'blog': blog,
        'categories': categories,
        'new_blogs': new_blogs,
        'old_blogs': old_blogs,
        'popular_blogs': popular_blogs
    })


def search_results(request):
    query = request.GET.get('q', '')  # دریافت پارامتر جستجو
    if query:
        # جستجو در عنوان و محتوای بلاگ‌ها
        search_results = blogs.objects.filter(
            title__icontains=query
        ) | blogs.objects.filter(
            content__icontains=query
        )
    else:
        search_results = blogs.objects.none()  # اگر جستجویی وجود ندارد، نتایج خالی

    return render(request, 'search_results.html', {
        'search_results': search_results,
        'query': query
    })


def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        customer = Customer(
            name=name,
            lastname=lastname,
            phone=phone,
            email=email,
            message=message
        )
        customer.save()
        return render(request, 'contactUs.html', {'success': True})
    else:
        return render(request, 'contactUs.html')


def Portfolio(request):
    filter_type = request.GET.get('filter', 'newest')

    if filter_type == 'popular':
        worksamples = OtherExample.objects.order_by('-popularity')
    elif filter_type == 'newest':
        worksamples = OtherExample.objects.order_by('-created')
    elif filter_type == 'oldest':
        worksamples = OtherExample.objects.order_by('created')
    else:
        worksamples = OtherExample.objects.all()  # حالت پیش‌فرض

    context = {'worksamples': worksamples}
    return render(request, 'Portfolio.html', context)


def singlePortfolio(request, id):
    cv = get_object_or_404(OtherExample, id=id)
    url_exists = bool(cv.url)
    portfolios = OtherExample.objects.all()[:4]

    # Query for desktop images
    images = cv.desktop_images.all()

    images_listDesc = []
    for image_set in images:
        if image_set.image1:
            images_listDesc.append(image_set.image1.url)
        if image_set.image2:
            images_listDesc.append(image_set.image2.url)
        if image_set.image3:
            images_listDesc.append(image_set.image3.url)
        if image_set.image4:
            images_listDesc.append(image_set.image4.url)

    # Query for mobile images
    images_mobile = cv.mobile_images.all()

    listImageMobile = []
    for image in images_mobile:
        if image.image1:
            listImageMobile.append(image.image1.url)
        if image.image2:
            listImageMobile.append(image.image2.url)
        if image.image3:
            listImageMobile.append(image.image3.url)
        if image.image4:
            listImageMobile.append(image.image4.url)

    return render(request, 'PortfolioPage.html', {
        'cv': cv,
        'image_url': cv.image.url,
        'title': cv.title,
        'description': cv.des,
        'url': cv.url,
        'time': cv.time,
        'tools': cv.tools,
        'language': cv.language,
        'pagecount': cv.pagecount,
        'created': cv.created,
        'generaldes': cv.generalـdes,
        'popularity': cv.popularity,
        'url_exists': url_exists,
        'portfolios': portfolios,
        'images_list': images_listDesc,
        'listImageMobile': listImageMobile
    })

# mobile_images = MobileImage.objects.filter(other_example=cv).first()  # Get the first related MobileImage instance

# # Prepare a list of available images
# images_list = []
# if mobile_images:  # Check if mobile_images is not None
#     if mobile_images.image_mobile1:
#         images_list.append(mobile_images.image_mobile1.url)
#     if mobile_images.image_mobile2:
#         images_list.append(mobile_images.image_mobile2.url)
#     if mobile_images.image_mobile3:
#         images_list.append(mobile_images.image_mobile3.url)
#     if mobile_images.image_mobile4:
#         images_list.append(mobile_images.image_mobile4.url)
