'''
pip install instaloader
'''
from instaloader import Instaloader, Profile 
L = Instaloader()

 #instagram username for profile you want to download data
PROFILE = "shamika_dixshit"
profile = Profile.from_username(L.context, PROFILE)
posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes,reverse=True)

#to download from only 2 posts
selected_range = posts_sorted_by_likes[0:78] 
for post in selected_range:
    L.download_post(post, PROFILE)

