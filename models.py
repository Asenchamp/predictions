from django.db import models
from django.contrib.auth.models import User #import user to modifine the choice model

# Create your models here.
# Question class

class League(models.Model):
    league_name = models.CharField(max_length=100)
    # Add any other fields relevant to your application

    def __str__(self):
        return self.league_name

class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, default=None)
    match_text = models.CharField(max_length = 300)
    match_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.match_text
    
class Option(models.Model):
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class Choice(models.Model):
    match = models.ForeignKey(Match, on_delete = models.CASCADE)
    choice = models.ForeignKey(Option, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    voter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Add this line

    
    def __str__(self):
        return self.choice.choice_text


"""
class Match(models.Model):
    match_text = models.CharField(max_length = 300)
    match_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.match_text

class Choice(models.Model):
    match = models.ForeignKey(Match, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    voter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Add this line

    
    def __str__(self):
        return self.choice_text

"""
"""
class Question(models.Model):
    question_text = models.CharField(max_length = 300)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
"""