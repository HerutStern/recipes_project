from django.db import models
from recipes_project_app.validators import validator_level


# Recipe

class Recipe(models.Model):
    name = models.CharField(max_length=256, db_column="name", null=False, blank=False),
    ingredients = models.CharField(max_length=500, db_column='ingredients',
                                   null=False, blank=False)
    instructions = models.CharField(max_length=500, db_column='instructions',
                                   null=False, blank=False)
    level = models.SmallIntegerField(max_length=10, db_column='level',
                                     validators=[validator_level])

    class Meta:
        db_table = 'recipe'

# Rating

# Create your models here.
