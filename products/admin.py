from django.contrib import admin

from products.models import Product, Lesson, ProductUser, UserLesson


class ProductUserLine(admin.TabularInline):
    model = ProductUser
    min_num = 1
    max_num = 200
    extra = 1


class UserLessonLine(admin.TabularInline):
    model = UserLesson
    min_num = 1
    max_num = 200
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductUserLine,)
    list_display = (
        'name',
        'description'
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = (UserLessonLine,)
    list_display = (
        'name',
        'link',
        'duration',
        'product'
    )
