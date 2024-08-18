Kinnect

Wireframes

User Stories

Features

Testing

*Link to TESTING.md*

Validator Testing

Lighthouse Testing

Bug Fixing:

- When running tests for the Post list, i discovered an error "ERROR: test_can_list_posts (posts.tests.PostListViewTests.test_can_list_posts)". Reading through the error message allowed me to rectify the issue and traceback to the Post.views file where the error persists because the request context was not being passed to the serializer in the PostListView.
- When going back through my work, i was testing the links for 'profiles', and 'posts' before moving forward into 'comments'. I discovered that the '/posts' address was throwing out and operational error for the post.image_filter that had been added. Saving the file and reloading the page, the error persisted. I then realised that it was added after the initial migration of the posts app and so i did 'python manage.py makemigrations' and then 'python manage.py migrate' and reloaded the website and saw that it had fixed the issue.

Unfixed Bugs


Deployment

Heroku Deployment

Preparing File for Deployment

Final Deploy

Credits

Media

