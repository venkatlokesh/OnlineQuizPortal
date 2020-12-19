from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Quiz(models.Model):
    quiz_id = models.IntegerField(default=None,unique=True,primary_key=True)
    quiz_name=models.CharField(max_length = 200)
    def  __str__(self):
        return str(self.quiz_id) + ','+str(self.quiz_name)

class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,default=None)
    question_id=models.IntegerField(default=None,unique=True,primary_key=True,validators=[MinValueValidator(1),MaxValueValidator(10)])
    question_name=models.CharField(max_length = 200)
    def  __str__(self):
        return str(self.quiz)+','+str(self.question_id)+','+str(self.question_name)
class Option(models.Model):
    question=models.ForeignKey(Quiz,on_delete=models.CASCADE,default=None)
    option_id=models.IntegerField(default=None,unique=True,primary_key=True,validators=[MinValueValidator(1),MaxValueValidator(4)])
    option_name=models.CharField(max_length = 200)
    is_answer=models.BooleanField(default=False)
    def  __str__(self):
        return str(self.question+','+self.option_id+','+self.option_name+','+self.is_answer)

