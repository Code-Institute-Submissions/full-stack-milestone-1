# Full stack development - Milestone Project - Seamless. Computer store.

The project is deployed on Heroku here - https://full-stack-milestone.herokuapp.com/


## UX
Seamless is an online eCommerce store thats allows you to purchase products, review prodiucts, reccomend upgrades and create accounts. 

I have created a simple layout that is easy to use and easy on the eye. I did not want to go over the top on design as the functionality of this project is the key.

I created wireframes using my preferred prototyping software, Adobe XD. The wireframes can be found in PDF format here - https://github.com/cobyfoster/full-stack-milestone/tree/master/media/designs
If the above link returns GitHub errors, refer to this dropbox link - https://www.dropbox.com/sh/ajjvjh70t7g7l4t/AAD_nIP5pnGR50zU17PfQD7La?dl=0

https://github.com/cobyfoster/full-stack-milestone/tree/master/media


## Apps
**Account**: <br>
I have added the ability for users to create an account on the site. This uses Django's allauth functionality to authenticate, confirm email addresses and to create the account in general. When logged in, users will be able to access their orders, saved delivery information and logout. SuperAdmins are able to create and delete products.

**Products**: <br>
Procducts are used in various ways. using products, I have created forms and models to review the products and also recomend upgrades for products that have the brand 'custom'. This is great for user interaction and will allow the site owner to take ideas from customers and build the custom computer. 
The products app is also used to pass data to the CART app. 

**checkout**: <br>
The checkout app is fully setup with stripe (testing / sandbox) to allow test purchases on the site. The app has custom webhook handles for different webhooks. They can be found int he webhook_handler.py file within the app. I have also set delivery logic. 

**Cart**: <br>
I have added the functionality for users to add Products to the cart. The data is then grabbed using the products ID (pk Django) and the relevant information is then displayed. 

**Home**: <br>
Home is a simple app for displaying the home page. 


## Features
**Review** <br>
I created a Review model within the Products app. This model is used to allow LOGGED IN users to leave reviews for products. This feature is great for user nteraction and to create confidence in your online store. I then created a form for this model using forms.py and integrated this with crispyforms.

**Upgrade** <br>
I created a Upgrade model within the Products app. This model is used to allow LOGGED IN users to leave recomendations for products that have the category 'custom'. This feature is great for user nteraction and to create confidence in your online store. I then created a form for this model using forms.py and integrated this with crispyforms.

**Search**<br>
I created a search bar that allows you to search for specific products by searching through its meta data. It can search fr the model_name, description, product specification and brand. It even allows you to search for the product type (laptop or PC)

**Sorting**<br>
Custom product sorting was added to allow users to sort by price, name, category ect. This allows them to find their desired product quicker. 

**Add Products**<br>
For Admins only! This allows admins to create products with a nice designed front end form. You can even upload images and it sends it straight through to AWS. 

**Edit Products**<br>
The edit Product function allows Admins to then edit the product information in the same form as described above. The form is pre-filled with the current information. 

**Delete Products**<br>
Does what it says on the tin. Accessed via URL and product id. For e.g products/delete/1. this will delete product with the ID/pk 1.


**navigation**<br>
Search bar is hidden until you click on the search bar. I have used Bootstraps navigation for dropdown. 

**Cart (added function)**<br>
Within the cart you can add or remove products as well as chage the quantity.

**Account (added function)**<br>
Within your account, you can view your previous orders. 

**Logic**:<br>
Overall, an extensive amount of logic is being used. It's used to search the database tables, as well as displaying relevant content depending on who is logged in. 


## Technologies Used

In the development of this project, I have used the following technologies.
- Python
- HTML5
- CSS / Bootstrap
- JS / JQuery
- SQL
- Django
- Heroku (for deployment)
- Stripe (payment gateway)
- Adobe XD (for mockups)
- Jinja Templating Language

Full stack list can be found in the requirements.txt file.

## Deployment
## Deployment
The website was coded in GitPod, an IDE used to easily work with GitHub. I started by creating my repository in GitHub then forming an initial commit with the message "initial commit". I then used "Git Push" to push this through to GitHub.

To deploy to Heroku, I first connected my database to Postgres. This allowed me to use 'loaddata' to upload my fixtures to the deployement server. I then disabled COLLECTSTATIC so that Heroku would IGNORE my static files. This is because I wanted to store them on AWS S3. So I then created my AWS Bucket named 'full-stack-milestone". After doing this, I set permissions to read for everyone, this makes the bucket public. Then, I changed the ACL to make it public. I then added the following to the CORS:

[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]

The, I generated a Bucket policy using AWS's policy generator. I added /* on the end of the recource name to allwo all files to be accessed. Then, using AWS's app IAM, I created a user group to manage the app. I then created a policy for the group and added a user to manage. I downloaded the keys / credentials and stored them within my config vars. 

Here is a list of my config vars within heroku;
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- DATABASE_URL
- EMAIL_HOST_USER
- EMAIL_HOST_PASS
- SECRET_KEY
- STRIPE_CURRENCY
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_WH_SECRET
- USE_AWS

Using my requirements.txt you can see I used psycopg2, dj_database_url, and boto3 for connections and deployement.

I have set some things to only run in DEVELOPMENT. These can be foudn in the settings.py file. For e.g, DEBUG = True for Deployment but not for Heroku. 

For emails, I have connected using SMTP to my personal Gmail account. This way when signing up and purchasing items, you will recieve emails from the server. (cobyfoster99@gmail.com)

I have enabled caching for AWS files, this is because they are not going to chaoge after deployement and it will speed up the site for past viewers. 


## testing

#### Responsive testing
To test the apps responsiveness, I did this 2 ways. 

1. Using Google's inspect elements device toolbar. I set it to responsive and changed between screen widths. 
2. I manually tested using my iPhone 12 Pro Max, my partners Samsung note 20 and an old iPhone 8 I had lying around. I then tested with my samsung Tab S6 and my partners iPad air. 

#### Browser testing 
To check browser compatibility, I navigated and used the site on the following browsers.
1. Google Chrome
2. Mozilla Firefox
3. Microsoft Edge
4. Opera
5. IE11 (deprecated)

#### W3C Validation & PEP-8 compliance
The GitPod IDE already has PEP-8 compliance helpers, it shows me when a line is too long or when the corret spaces are not applied. I then went to http://pep8online.com/ and entered all of my code (several checks, one for each doc). I then checked URL's using https://validator.w3.org/.

#### Google Lighthouse
The report as follows. 

1. Performance 74/100
A good score!

2. Accessibillity 81/100

3. Best practices 93/100!
Amazing score, very happy with this.

4. SEO 82/100. I would of liked to improve this by creating a SLUG for each product. I'd do this by getting the product name, removing the spaces and replace with -. The POST this to the slug. Then eahc product page's URL with be the product name! Great for SEO!

Overall, i'm happy with the results but there is room for improvement. 


#### Functionality testing
I first tested the Django app after starting the project. I was happy to see Django screen to say that it has been successfull!

Then, I wanted to test my all_products view. To do this, I requested product information and displayed it in a query o the products page. Product ID's were displayed! This means I am connected to the SQL database properly.

To ensure the server response was correct in my automatic testing, I want to my Heroku project to confirm it was working as expected. 

Outcome - The correct data was visible and the connection to GITHUB master branch was working correctly.

3rd Party testing - I then asked my partner to test the websites functionality. I did not give her any guidance on how to use the website, instead I gave her the mouse and told her to use it as if it were a standard Ecommerce website. 

Quote - "The website was really easy to use and allowed me to create an account to view my orders. The order process was very simple and I tested this with a test cart number 4242ect. I would recomend increasing the size of the home page to allow people to find products straight away instead of having to look".

I ran the website through a site_crawler that checked for any missing links, there were multiple missing links at the time so I swiftly fixed this before deployement. 

#### Views testing
I manually tested all functionality on the website. 

1. Add to cart
2. Checkout
3. Review
4. Upgrade
5. Cart
6. Add, delete, edit Products and Categories.



## Credits

### Code
I followed the CodeInstitute tutorials to achieve some of the functionality. I was able to re-use some of the mini-project. This worked in cases like Stripe as the functionality is the exact same for the 2 projects. I also followed Stripe docs to create the functionality. https://stripe.com/docs/stripe-js

I also used Bootstrap to swiftly build the layout of the website. https://getbootstrap.com/docs/5.0/getting-started/introduction/

### Content
Products content and images were taken from https://www.cyberpowersystem.co.uk/
All credit to them for image quality.

