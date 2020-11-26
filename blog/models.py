from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)


class Post(models.Model):
    title= models.CharField(max_length=225)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True) #auto_now_add assisgn the current date and time to this field whenever a instance is created
    last_modified=models.DateTimeField(auto_now=True) #auto_now assigns the current date and time to this field whenever an instance of the class is saved. This mean whenever you edit an instance of class, the date_modified is updated
    categories=models.ManyToManyField('Category',related_name='posts') # ManyTOMany field type make a relationship between 2 tables.
    #ManyToMany field take 2 arguments. First, the model with which the relatioship is (Category)
    #Second argument allows us to access the relationship from a 'Category object'. 
    #Many categories is assigned to many posts

class Comment(models.Model):
    author=models.CharField(max_length=60)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey('Post',on_delete=models.CASCADE)
    #Relationship= Many comments can be assigned to one post
    #But can't have a comment correspond to many posts
    #ForeignKey field take 2 arguments. First is the other model in the relationship, which is 'Posts'. Second tells django to what to do when the post is deleted
    