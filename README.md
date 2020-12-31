# Tralee United FC Website
![Tralee United Intro](../master/readme-images/intro.png "Tralee United FC Intro")
## Introduction
For my fourth and final project I’ve created a website for a fictional football club - Tralee United - based in my hometown of Tralee. I decided to select this type of website for my project because a club website can include many different sections such us blog-type news section, shopping page with club’s gear, membership forms etc., just so I can learn to use as many functions of the framework as possible.
The site is built using Django framework, with Bootstrap CSS framework for layout and JavaScript for interactivity, payments verifications.

The live version of the project can be view at: [Tralee United App](https://tralee-united.herokuapp.com/)

## UX
### User Stories
The site can be viewed by different kind of visitors, looking for completely different information. I’ve split the stories into groups - club fans, club members, site admins
#### Club Fan User
- I want to be up to date with what’s going on with the club
- I want to browse previous posts to see the historical information about the club
- I want to support my Club and purchase various merchandise products
- I want to send a message to Club admin using contact form
#### Club Member
- I want to join the club using a membership form
- I want to purchase necessary gear with club branding
- I want to pay online and receive the items delivered to a given address
- I want to login and see my previous orders
#### Site Admin
- I want to login to dedicated admin area of the site
- I want to manage items in the shop - add, remove, set prices
- I want to receive notifications about online orders
- I want to receive notification when somebody sends a query via contact form or fills in the membership form
### Strategy
The goal of the project was to create a portal for a football club where: 
- fans can check news from a club
- fans and members can buy various club gear and merchandise
- site visitors can send a message using a contact form
- future members can send their application using sing up form
- site admins can manage the shop, applications and contact form messages
### Scope
My previous experience building Wordpress based websites for local sports clubs helped me to pick the right features for a functional club website. The news section, club on-line shop and membership form were the most requested features thus I wanted to make sure they are fully functional and easy to use.
### Structure
Django breaks down all functional sections of the site into separate ‘apps’, the project consists the following apps:
- Homepage with news teasers, random selection of products
- News section with timeline view and individual posts pages
- Shop section with main shop view and individual products pages
- Basket section, responsible for on-line shopping, adding products, adjusting quantities before purchase
- Checkout section, responsible for finalising the order, taking payments, creating orders in the back-end
- Contact page, with contact form 
- About us page, showing image slider and short club history
- Membership page, with membership form
### Skeleton
The mockups were created using Balsamiq app. Below is the selection of various screens in desktop and mobile formats:
- Homepage: [Desktop](../master/readme-images/Homepage.png), [Mobile](../master/readme-images/Mobile-Homepage.png)
- News timeline: [Desktop](../master/readme-images/News.png)
- News post: [Desktop](../master/readme-images/News-Item.png)
- Shop page: [Desktop](../master/readme-images/Shop.png), [Mobile](../master/readme-images/Mobile-Shop.png)
- Product page: [Desktop](../master/readme-images/Product.png), [Mobile](../master/readme-images/Mobile-Product.png)
- Basket page: [Desktop](../master/readme-images/Basket.png)
- Checkout page: [Desktop](../master/readme-images/Checkout.png)
## Development
- The developments start with the installation of Django package using `pip3 install django` command in the project folder
- Django needs a database to run so the next thing to do is to create one using `python manage.py migrate` command, which later is used to update database structure
- Each element of the website is contain inside Django app. To create an app I’ve used `startapp` command. Each command needs to follow `python manage.py` in order to run
- Each app needs to be connected to main project app via settings, urls files
- At later stage of the development the site was deployed on Heroku cloud server using its direct link to my GitHub repository 
- In order to run Python applications on Heroku, 2 files need to be created - `requirements.txt` which lists all packages used on the project and `Procfile` which tells Heroku what kind of application it is and how to run it
- Heroku does not allow sqlite files to be used so I needed to move the database into Heroku add-on PostgreSQL server, adding login credentials into main settings file
- Amazon S3 store server was used to store status files and images. S3 allows to create containers for the files called buckets. Following the guide in the module I’ve created a bucket for the project, setup necessary permissions and public access rules. The application successfully transferred all initial files into the bucket and keep uploading all new files as I create new content.
- The application uses Stripe as the test payment platform. I’ve used my existing account and used test API keys make test transactions 
## Deployment
- The project was started on local machine. I’ve used PyCharm as my main code editor. It’s much more robust than previously used VS Code and it has some built in Django functionality (code hinting, functions and method names autocompletion). 
- As with the previous project I’ve used a virtual environment to encapsulate the project, Python interpreter and all used extensions to just project folder.
- The application was linked to remote repository on Github, all code changes were committed locally and then uploaded to remote repository
- During the initial stages of development the application used Sqlite database to hold the information. All static files (images, style sheets, scripts) were stores locally.
- Once all main parts of the application were up and running I’ve deployed it on Heroku cloud server, database moved to PostgreSQL and all static files moved to Amazon S3 bucket
- Heroku application was linked to application’s Github repository with automatic deployment enabled
- Django allows to have different application environment for local and remote copies. The downside of this approach is that all content has to be created in both places. This was the case with shop and blog sections, superuser account
- The finished project can be installed locally using `git clone https://github.com/redlik/django_sportclub_m4.git `command. This will copy all project files into local folder.
- To make the application fully running, a user needs to install Django package with `pip3 install django` plus all packages used with `pip3 install -r requirements.txt` command
- Next, the database needs to be initialise with `python3 manage.py migrate`
- The application needs bunch of variables set up in system environment, such us Stripe API keys, Amazon S3 credentials, debug flags, all listed in the main `settings.py` file. Check how you particular OS manages system environment variables 
## Testing
- During the whole development process I was using PyCharm built in code checkers and formatters. I’ve also tested the website on ww3 html and css validators. Both were passed successfully
- For the real device testing I’ve used a selection of devices, iPhones, iPad and Samsung Galaxy phone. No major issues with the layout was observed

To test the app logic I’ve followed the user scenarios to make sure all functionality is working as planned:
- After creating a superuser I’ve tested the backend, using `/admin` url. I was able to login and see the models I’ve created
- I tested the CRUD functions on the backend. I was able to create, update and delete all models of the application
- Following the module on user profile app I’ve noticed a small issue - when a superuser is created, it doesn’t create a new profile. This caused the application to crash when superuser credentials were used to regular login.
- The solution for that was to login to the database directly and create new, empty profile for the superuser ID

Next, I’ve tested the shop section, consisting of product, basket, checkout, profile apps
- The shop page displays all products correctly, the category filter works as expected
- On product detail page the basket functionality works as expected, I was able to add product to basket, select size and quantity
- The correct subtotal is being calculated on the basket widget
- The checkout page correctly displays the basket contents, prices, delivery details (free for over €100, €5 if less)
- The payment form uses Stripe test API keys, each correct transaction using Stripe test card numbers resulted in the payment recorded on Stripe Dashboard
- The application uses Stripe webhooks to send back successful or failed payment attempts. All events were caught by special url `checkout/wh` and orders were recorded in database 
- If the transaction is done with logged in user the delivery details are saved inside user profile record. Same information is used to fill in the form on subsequent transactions

After that I’ve tested both contact and membership forms
- Both forms correctly display selected fields, thanks to Crispy Forms package all fields follow Bootstrap styling and required fields are marked with `*`
- The date field on the membership form was displayed as text by default so I’ve used a small JavaScript command to change its type to ‘date’ as most of the modern browsers support the calendar widget on date field
- Both forms are linked to their Models and all entries are saved in the database. On top of that a dedicated ‘Admin’ email gets a notification after each entry
## Features not implemented
- When the site admin changes status of the application from 'Candidate' to 'Member' I'd like to send a welcome email to the application sender
- Protect all forms with HoneyPot or ReCaptcha to prevent spam emails being sent 
## Credits and Acknowledgements
- All blog posts were taken from a selection of Irish football club websites
- Club history text was taken from Drogheda United website
- All images come from royalty-free services such us Unsplash, Pexels
- Product mockups were done using various Photoshop mockups I have in my stock library