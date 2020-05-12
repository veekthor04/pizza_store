# Project 3

Web Programming with Python and JavaScript

My Pizza kitchen a web application for handling a pizza restaurant’s online orders. 
Users can browse the restaurant’s menu, add items to their cart, and submit their 
orders. The restaurant owner can add and update menu items, and view orders that have
been placed. 


Additional infomation: 

Admin mamagement: the admin can add products via '/admin/'
the admin can view and print order details via '/admin/checkedout/order/' 

Personal Touch: the app supports sending users a confirmation email once their 
purchase is complete.

Environmental variables used are:
EMAIL_HOST,
EMAIL_HOST_USER,
EMAIL_HOST_PASSWORD


Files info: 

main;

main/manage.py: this is the main file that runs the web application. 

main/requirements.txt: contains the dependencies required for the web application to
run. 
main/README.md: contains info about the app.

main/db.sqlite3: contains the database for the project.

main app;

main/pizza/celery.py: this file is used to set environmental variable for celery to 
monitor mail task.

main/pizza/settings.py: this contains the settings for the project.


main/pizza/urls.py: links all routings in the project together.

main/pizza/wsgi.py

orders app;

main/orders/migrations folder:

main/orders/static/css/base.css: contains the style sheet for base.html

main/orders/static/pic/...: contains all pictures used in the web application

main/orders/templates/orders/product/detail.html: displays the detail about a specific
product with the option to include topping(for pizza only),select quantity and add to 
cart.

main/orders/templates/orders/product/list.html: displays all products available in the
database with option to group by category.

main/orders/templates/orders/base.html: contains the base templates used to avoid
repetitions.

main/orders/admin.py: allows admin to add, edit and monitor each product.

main/orders/apps.py: sets the app config name

main/orders/models.py: contains the models for the app, which are category,product,
and topping.

main/orders/tests.py: no test was included for the app.

main/orders/urls.py: contains the url routes for the app.

main/orders/views.py: contains the processes during routing in the app.

cart app;

main/cart/migrations folder: contains all migration carried out after the app's models
file was created.

main/cart/templates/cart/detail.html: display all products added to cart, prices,
toppings( if added) option to checkout or continue shopping.

main/cart/admin.py: no admin code for this app.

main/cart/apps.py: sets the app config name.

main/cart/cart.py: contains the processes for keeping record of the session detail of
user and products added to cart with calculated amounts.

main/cart/context.py: displays the cart summary at the top or the base page.

main/cart/forms.py: contains the forms required in the detail.html page.

main/cart/models.py: no models for this app.

main/cart/tests.py: no test was included for the app.

main/cart/urls.py: contains the url path for contains the url routes for the app.

main/cart/views.py: contains the processes during routing in the app.

account app;

main/account/migrations folder: contain all migration carried out after the app's models
file was created.

main/account/templates/account/login.html: displays the page which allows users to 
enter their login details.

main/account/templates/account/register_done.html: displays the page which shows user
registration is complete.

main/account/templates/account/register.html: displays the page which allows users create
their account.

main/account/templates/registration/logged_out.html: displays the page that shows if
logout is successful.

main/account/templates/registration/login.html: displays the page that tells user if
his credentials are incorrect.

main/account/admn.py: no admin code for this app.

main/account/apps.py:sets the app config name.

main/account/forms.py: contains the login and registration forms.

main/account/models.py: no models was created for the app.

main/account/test.py: no test was created for the app.

main/account/urls.py: contains the url path for contains the url routes for the app.

main/account/views.py: contains the processes during routing in the app.

checkedout app;

main/checkedout/migrations folder: contain all migration carried out after the app's 
models file was created.

main/checkedout/templates/admin/checkedout/order/datail.html: display datail about
orders made to the admin.

main/checkedout/templates/checkedout/order/create.html: displays the page which
allows users to enter shiping info to finalise order.

main/checkedout/templates/checkedout/order/created.html: displays the page which
tells user thats order has been placed and shows order ID.

main/checkedout/admin.py: contins the processes for the admin page to view order 
items, order info, option to export to csv...

main/checkedout/apps.py: sets the app config name.

main/checkedout/forms.py: contains the form which allows user to enter his shipping
details.

main/checkedout/models.py: creates the model for the order items and shipping info.

main/checkedout/task.py: contains the task to send maail to user view the shiping
mail provieded.

main/checkedout/tests.py: no test creates for the app.

main/checkedout/urls.py:  contains the url path for contains the url routes for the 
app.

main/checkedout/views.py: contains the processes during routing in the app.