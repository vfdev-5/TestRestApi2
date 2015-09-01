
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





