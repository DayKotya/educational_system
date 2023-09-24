from rest_framework import serializers

from products.models import Lesson, Product


class LessonSerializer(serializers.ModelSerializer):
    viewed_time = serializers.SerializerMethodField()
    is_viewed = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = (
            'name',
            'link',
            'viewed_time',
            'is_viewed',
            'last_viewed_date'
        )

    def get_viewed_time(self, obj):
        user_lesson = obj.user_lesson.first()
        if user_lesson:
            return user_lesson.viewed_time
        return None

    def get_is_viewed(self, obj):
        user_lesson = obj.user_lesson.first()
        if user_lesson:
            return user_lesson.is_viewed
        return False

    def get_last_viewed_date(self, obj):
        user_lesson = obj.user_lesson.first()
        if user_lesson:
            return user_lesson.last_viewed_at
        return None


class ProductSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'name',
            'lessons'
        )

    def get_lessons(self, obj):
        lessons = obj.lessons.all()
        lesson_serializer = LessonSerializer(
            lessons,
            many=True,
            context=self.context
        )
        return lesson_serializer.data
