from services import wp_api
# Set the data for the new post as a dictionary
post_data = {
    'title': 'Game of thrones',
    'content': """
           Test 3
    """,
    'status': 'publish'
}

wp_instance = wp_api.Post('https://www.financechit.com/wp-json/wp/v2/posts')

################################################################################################

# GET All published post
for post in wp_instance.get_posts():
    print(post['id'])

################################################################################################

# POST Create all post

# created_post = wp_instance.create_post(post_data)
# print(created_post)

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