from django.urls import path

from recipes_project_app import views

urlpatterns = [
    path('add_recipe', views.add_recipe),
    path('get_all_recipes', views.get_all_recipes),
    path('get_recipe_by_id/<int:recipe_id>', views.get_recipe_by_id),
    path('delete_recipe_by_id/<int:recipe_id>', views.delete_recipe_by_id),
    path('edit_recipe/<int:recipe_id>', views.edit_recipe)
]