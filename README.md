
# Test REST Api

Example of REST Api with users
- Django
- Django REST Framework
- ...

## API description :

The api stores photos/comments that authenticated users can upload to the api.
#### Any user can request all images
    (GET) <URL>/api/photo/

or a particular image by its id, e.g:

    (GET) <URL>/api/photo/1/

#### Any user can request all comments
    (GET) <URL>/api/comment/


#### Authenticated user can get its token (using CURL):

    curl -X POST
         -H 'Content-Type: application/json'
         -d '{"username":"your_username", "password":"your_password"}'
         <URL>/api/auth-token/

The response looks like : 
    
    {"token":"20bc9.......82ee"}

#### An authenticated user can upload an image:

    curl -S <URL>/api/photo/
            -F "image=@/path/to/file.jpg;filename=uploaded_file_name.jpg;type=image/*"
            -H 'Authorization: Token <user_token>'

#### An authenticated user can create a comment:

    curl -X POST 
         -H 'Content-Type: application/json' 
         -d '{"comment":"This is another test comment created by a user"}' 
         -H 'Authorization: Token <user_token>'
         <URL>/api/comment/


### Useful info
On OAuth2 :

<a href="http://www.slideshare.net/aaronpk/an-introduction-to-oauth2?related=1">aaronpk : an-introduction-to-oauth2</a>

In case of
<a href="http://stackoverflow.com/questions/24377506/httperror-403-forbidden-with-django-and-python-social-auth-connecting-to-googl">HTTPError 403 (Forbidden) with Django and python-social-auth connecting to Google with OAuth2</a>

Catch AuthCanceled exception :
http://stackoverflow.com/questions/20907276/python-social-auth-authcanceled-exception


### TODO
03/09/2015

- OK = Login as github/google user using a link from test html
- OK = Logout user using a link from test html
- OK = Display Login/Logout options on the test html
- OK = Convert 3rd party token to my Api token

04/09/2015
Client side :
- Obtain user details from 3rd party social oauth resource using AJAX
- Convert tokens using AJAX 






