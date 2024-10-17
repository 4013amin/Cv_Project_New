from django.db import models
from jalali_date import date2jalali, datetime2jalali


class OtherExample(models.Model):
    image = models.ImageField(upload_to="otherexamples")
    image_mobile = models.ImageField(upload_to="otherexamples", null=True)
    title = models.CharField(max_length=200)
    des = models.TextField()
    generalـdes = models.TextField(null=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200, null=True)
    tools = models.CharField(max_length=200, null=True)
    language = models.CharField(max_length=200, null=True)
    pagecount = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    popularity = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title


class ImageOtherExample(models.Model):
    otherExample = models.ForeignKey(OtherExample, related_name='desktop_images', on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="otherExampleImages", null=True, blank=True)
    image2 = models.ImageField(upload_to="otherExampleImages", null=True, blank=True)
    image3 = models.ImageField(upload_to="otherExampleImages", null=True, blank=True)
    image4 = models.ImageField(upload_to="otherExampleImages", null=True, blank=True)

    def __str__(self):
        return f"Image of {self.otherExample.title} - {self.id}"


class ImageOtherExampleMobile(models.Model):
    otherExample = models.ForeignKey(OtherExample, related_name='mobile_images', on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="otherExampleImages", null=True, blank=True)
    image2 = models.ImageField(upload_to="otherExampleImages", null=True, blank=True)
    image3 = models.ImageField(upload_to="otherExampleImages", null=True, blank=True)
    image4 = models.ImageField(upload_to="otherExampleImages", null=True, blank=True)

    def __str__(self):
        return f"Image of {self.otherExample.title} - {self.id}"


# class MobileImage(models.Model):
#     other_example = models.ForeignKey(OtherExample, related_name='mobile_images', on_delete=models.CASCADE)
#     image_mobile1 = models.ImageField(upload_to="otherexamples/mobile", null=True)
#     image_mobile2 = models.ImageField(upload_to="otherexamples/mobile", null=True, blank=True)
#     image_mobile3 = models.ImageField(upload_to="otherexamples/mobile", null=True, blank=True)
#     image_mobile4 = models.ImageField(upload_to="otherexamples/mobile", null=True, blank=True)
#
#     def __str__(self):
#         return f"Mobile Image for {self.other_example.title}"


class Cv(models.Model):
    url = models.URLField(max_length=200)
    time = models.CharField(max_length=200)
    tools = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    pagecount = models.IntegerField()
    otherexamples = models.ForeignKey(OtherExample, on_delete=models.CASCADE, related_name="cv_examples", null=True)

    def __str__(self):
        return self.url


class Customer(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class CategoryWeblog(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class blogs(models.Model):
    image = models.ImageField(upload_to='blogs/')
    imageContent = models.ImageField(upload_to='blogs/content', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # فیلد تاریخ ایجاد
    popularity = models.IntegerField(default=0, null=True)  # فیلد محبوبیت
    category = models.ForeignKey(CategoryWeblog, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)

    def get_jalaliData(self):
        return date2jalali(self.created_at)

    def __str__(self):
        return self.title
