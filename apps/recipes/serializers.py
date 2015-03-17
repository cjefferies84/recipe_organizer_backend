from rest_framework import serializers
from models import *


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review

    # def get_reviews(self, obj):
    #     reviews = Review.objects.filter(recipe=object.dataId)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment

    def get_comments(self, current_recipe):
        comment = Comment.objects.filter(recipe=current_recipe.id)
        serializer = CommentSerializer(comment, many=True)
        return serializer.data


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    # reviews = serializers.SerializerMethodField()
    # comments = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        tags_data = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients_data:
            try:
                ingredient = Ingredient.objects.get(name=ingredient["name"])
            except Ingredient.DoesNotExist:
                ingredient = Ingredient.objects.create(**ingredient)
            recipe.ingredients.add(ingredient)

        for tag in tags_data:
            try:
                tag = Tag.objects.get(name=tag["name"])
            except Tag.DoesNotExist:
                tag = Tag.objects.create()
            recipe.tags.add(tag)
        return recipe
