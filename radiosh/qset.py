

from radiosh.models import Post
from django.contrib.auth.models import User
me = User.objects.get(username='osama')

Post.objects.create(author=me, title='Sample title', text='Test')

Post.objects.all()


post = Post.objects.get(title="Sample title")
post.publish()