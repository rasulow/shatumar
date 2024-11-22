from modeltranslation.translator import translator, TranslationOptions
from . import models


class BaseTranslationOptions(TranslationOptions):
    fields = ('name', 'description')    
    

class BannerTranslationOptions(TranslationOptions):
    fields = ('title',)
    

translator.register(models.Category, BaseTranslationOptions)
translator.register(models.Product, BaseTranslationOptions)
translator.register(models.Banner, BannerTranslationOptions)
translator.register(models.Gallery, BannerTranslationOptions)
translator.register(models.Certificates, BannerTranslationOptions)


