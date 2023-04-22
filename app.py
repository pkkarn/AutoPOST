import sys
sys.path.insert(0, "./services")
from services import wp_api
from services import post_ai
from dotenv import load_dotenv
import os
load_dotenv()

wordpress_url = os.environ.get('wordpress_url')


post_title = input("Enter Post Title: ")

response_content = post_ai.writeSequenceArticle(post_title)
response_tags = post_ai.tags(post_title)

# Set the data for the new post as a dictionary
post_data = {
    'title': f'{post_title}',
    'content': response_content,
    'status': 'draft',
}

wp_instance = wp_api.Post(f'{wordpress_url}/wp-json/wp/v2/posts')

################################################################################################

# GET All published post
for post in wp_instance.get_posts():
    print(post['id'])

################################################################################################

# POST Create all post

created_post = wp_instance.create_post(post_data)
print(created_post)

################################################################################################

# DELETE DELETE Single post

# deleted_post = wp_instance.delete_post(13)
# print(deleted_post)

################################################################################################

# UPDATE Update Single post

# updated_post = wp_instance.update_post(20, {
#     "title": "Update Title",
#     "content": "tell me something boy"
# })

# print(updated_post)