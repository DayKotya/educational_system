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
            'is_viewed'
        )

    def get_viewed_time(self, obj):
        user = self.context.get('request').user
        user_lesson = obj.user_lesson.filter(user=user).first()
        if user_lesson:
            return user_lesson.viewed_time
        return None

    def get_is_viewed(self, obj):
        user = self.context.get('request').user
        user_lesson = obj.user_lesson.filter(user=user).first()
        if user_lesson:
            return user_lesson.is_viewed
        return False


class ProductSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'name',
            'lessons'
        )

    def get_lessons(self, obj):
        lessons = Lesson.objects.filter(product=obj)
        lesson_serializer = LessonSerializer(
            lessons,
            many=True,
            context=self.context
        )
        return lesson_serializer.data
