## Testing 

### Validator Testing - Python
No errors were found whne passing through the [CI Python Linter](https://pep8ci.herokuapp.com/#). All files below were passed through the linter bar some exceptions such as blank space and no new line at end of file: 
- comments app:
    - apps.py
    - models.py
    - serializers.py
    - urls.py
    - views.py 
- notifications app:
    - apps.py
    - models.py
    - serializers.py
    - urls.py
    - views.py
- likes app:
    - apps.py
    - models.py
    - serializers.py
    - urls.py
    - views.py 
- posts app:
    - apps.py
    - models.py
    - serializers.py
    - urls.py
    - views.py
- profiles app:
    - apps.py
    - models.py
    - serializers.py
    - urls.py
    - views.py 
- kinnect_api app:
    - asgi.py
    - permissions.py
    - serializers.py
    - settings.py
    - urls.py
    - views.py
    - wsgi.py

### Manual CRUD Testing

Comments:
    - logged in user can create a comment:
        - associated with a post
        - free text content field
    - owner of a comment can edit and delete their own comment:
        - post field cannot be edited
        - free text content field can be edited
        - comment can be deleted

Likes:
    - logged in user can create a like
        - each like is associated with:
            - comment
            - post
    - owner of a like can delete their own like

Posts:
    - logged in user can create a post:
        - free text notes field
    - owner of a post can edit and delete their own post:
        - currently playing boolean field can be edited
        - completed boolean field can be edited
        - notes field can be edited
        - post can be deleted
Profiles:
    - profile is automatically created when a new user signs up
    - owner of a profile can edit or delete their own profile:
        - name free text field can be added
        - description free text field can be added
        - image can be added

Notifications:
    - logged in users can see a notification:
        - bell icon displays number of notifications and what they are for when clicked

#### **Testing URLs**

| **URL** | **Passed** |
| --- | --- |
| roots | ✅ |
| /profiles/ | ✅ |
| /profiles/:id/ | ✅ |
| /posts/ | ✅ |
| /posts/:id/ | ✅ |
| /posts/create/ | ✅ |
| /followers/ | ✅ |
| /followers/:id/ | ✅ |
| /likes/ | ✅ |
| /likes/:id/ | ✅ |
| /notifications/ | ✅ |
| /notifications/:id/ | ✅ |
| /notifications/:id/delete/ | ✅ |