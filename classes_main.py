from classes_user import User
from classes_post import Post

app_user_1 = User("nn@nn.com", "Jan Vodicka", "pwd1", "DevOps Engineer")
app_user_1.get_user_info()

app_user_2 = User("jj@jj.com", "James Bond", "psw2", "Agent")
app_user_2.get_user_info()

new_post = Post("On a secret mission today", app_user_2.name)
new_post.get_post_info()
