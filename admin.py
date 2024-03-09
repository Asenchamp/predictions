from django.contrib import admin
from .models import Match, Choice, League, Option

admin.site.site_header = "The Arsene"
admin.site.site_title = "Arsene Admin Area"
admin.site.index_title = "Welcome !!!!"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 5
    fields = ['choice', 'votes']

    def get_formset(self, request, obj=None, **kwargs):
            formset = super().get_formset(request, obj, **kwargs)
            if obj:  # If editing an existing Match instance
                formset.form.base_fields['choice_text'].queryset = Option.objects.all()
            return formset

class MatchAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['match_text','league']}), ('Date Information', {'fields': ['match_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(League)
admin.site.register(Match, MatchAdmin)
admin.site.register(Option)

# Register your models here.
"""
from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "The Poll Mall"
admin.site.site_title = "Voting Admin Area"
admin.site.index_title = "Welcome to our Voting Admin Area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
"""