from modeltranslation.translator import translator, TranslationOptions
from . import models


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')    
    
    
translator.register(models.Category, CategoryTranslationOptions)


