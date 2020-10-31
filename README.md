# VirtualGym

Struggling to gain weight? or Gained a few extra kgs during lockdown? This site is to help you out with it. 
Waiting for you is a customised excercise and nutrition plan-all you need to get back in shape at home.


Subscribe and see other members reach their targets.  
#motivate_and_get_motivated.

Stay safe and workout at home 

## UX

This service is created keeping into consideration both weight gain and weight loss.
The user is provided with 3 subscription options to choose from, depending on their needs. 


Below are some user stories :
1. __User wants to signup :__   
    User will choose the signup option from the navigation, fill the fields and click on the signup button. if the field values are valid, a confirmation
    email will be sent to the user. Upon confirmation, the user's information will be stored on their profile page

1. __User wants to login :__   
    User chooses login from navigation, will be redirected to the login form. The user will enter the details and press on submit. If the values are correct,
    the user will be logged in to the system

1. __User wants to update his profile :__   
    User clicks on my account in the navigation, chooses profile. Updates the desired fields, If the values entered are valid, a success message will be displayed.
    If not an error message will be displayed.

1. __User wants to buy a product :__  
    User chooses the desired option from the shop button in the navbar then selects the product which takes the user to the product detail page.
    User can then choose the size (if applicable) and the quanity and click on add to bag. Here user can update his/her bag contents by changing the quantity
    and clicking on update or clicking on remove to delete the item from the bag. User then clicks on the checkout button, which will ask the customer to 
    enter details. If the card details are wrong, an error message will be displayed and if the payment is successful, a confirmation message will be displayed,
    which will contain all the order and delivery details 
      
2. __User wants to rate an item:__  
    User logs in. User chooses the desired option from the shop button in the navbar then selects the product which takes the user to the product detail page.
    User then clicks on add rating. A pop up will appear, the user then clicks on the stars and clicks on submit. If submitted without rating, an error
    message will appear, telling the user that the minimum rating is 1. If submitted with rating, the values are stored and the user is redirected to the all product page

1. __User wants to view the previous order :__ 
    User will login from the navigation, go to the profile page, if there have been orders made in the past, the details will be displayed in the table 
    next to their delivery information

1. __User wants to buy a subscription :__ 


1. __User wants to cancel a subscription :__ 


1. __User wants to view activity board :__ 

1. __User wants to log out :__ 
    User chooses the logout option from the navigation, a page will be displayed asking the user if they are sure, if yes they will be logged out of the system.
    If the user clicks on cancel the user will still be logged in


__During the early stages, a rough__ [wireframe](static/pdf/ .pdf) __was made using balsamiq__  


## Features

### Existing Features:
Navigation: allows the user to choose between what they want to acheive by clicking on the tab (code in: base.html).

Buy products: allows users to buy a product by entering the checkout form (code in: checkout app)

sort: allows users to sort the products depending on the name and price (code in: products app)

rating: allows the user to rate the products if they have logged in (code in: product app)

profile: allows the user to view their user details and the order details (code in: profile app)

save details: allows the user to save their checkout information (code in: checkout app)

subscribe: allows the users to choose from 3 subscription plans and choose the period of payment

activity board: allows the users to view the progress of other members

login/signup: allows the users to login to an account/create an account to buy products and services by filling out 
the username and password

### Features Left to Implement
* Have a chart to display the activity board information in a more user friendly way 
* Allow user to give a written review
* Display all the reviews with the dates and username
* Display product deals
* calculate BMI instead of asking the user
* If there are no orders linked to a user, in the profile page, display a message and a link to shop instead than an empty table
* Display a message to let the user know that the rating has been saved

## Technologies Used

**HTML:** Hypertext Markup Language (HTML) was used to create the webpage. 

**CSS:** Cascading Style Sheets (CSS) was used to add customised styling to the webpage.

**JavaScript:**  JavaScript enables interactive web pages and is an essential part of web applications. It was used to add interactive functionality to the webpage

**Python:** Python was used for the server side web development. Also to connect to the database and perform various operations of its data.

**Django:** [Django](https://www.djangoproject.com/) is a python based framework which was used in this project as it follows the Model Template View architectural pattern

**Bootstrap:** [Bootstrap](https://getbootstrap.com/) was used to create responsive webpages with the help of pre built classes

**FontAwesome:** [FontAwesome](https://fontawesome.com/) was used for icons

**Stripe:** [Stripe](https://stripe.com/gb?utm_campaign=paid_brand-UK%20%7C%20en%20%7C%20Search%20%7C%20Brand%20%7C%20Stripe&utm_medium=cpc&utm_source=bing&utm_content=&utm_term=EXA_Stripe%20General-stripe-e&utm_adposition=&utm_device=c&utm_content=xR7wn1XB-dc|pcrid|79164938360905|pkw|stripe|pmt|be|slid||productid||pgrid|1266637841642678|ptaid|kwd-79165156391371:loc-188|&msclkid=080ea1556ff41fee9c45fec9d0e69058)
was used to implement single and subscription payment methods.

**Balsamiq:** [Balsamiq](https://balsamiq.com/) was used to create wireframe. It was used in the initial stages of the project visualisation. It was used to put the idea of a page decide the layout and flow of the project. 

**JQuery:** [JQuery](https://jquery.com/) was used to simplify DOM manipulation.

## Testing

Manual testing was done on all the forms of this project

**Sign form:**  
Try to submit the empty form and verify that an error message about the required fields appears.  
Try to submit the form with invalid field values and verify that a relevant error message appears.  
Try to submit the form with user details already present in the database and verify that a relevant error message appears.  
Try to submit the form with all inputs valid and verify that the values get stored in the database. 

**Login form:**   
Try to submit the empty form and verify that an error message about the required fields appears.  
Try to submit the form with invalid field values and verify that a relevant error message appears.  
Try to submit the form with user details not present in the database and verify that a relevant error message appears.  
Try to submit the form with all inputs valid and verify that the success message appears. 

**Checkout form:**  
Try to submit the required fields with no data and verify that an error message is displayed.  
Try to submit the form with incorrect bank details and verify that an error message is displayed.

**review modal**
Try to submit the modal with no ratings and verify that an error message appears.
Try to choose a rating and leave the modal without submit and verify that the product doesnt have that rating stored.  
Try to submit the modal with some rating and verify that the rating gets saved


**Add product:**  

**Delete product**

**Edit product**

**review modal**

## Deployment

This project is used using [Heroku](https://dashboard.heroku.com/apps).  
Steps taken to deploy this project are as follows:  
* Create an app in Heroku  
* In the terminal typed the follow commands:  
    1. heroku login  
    1. heroku apps
    1. git init
    1. pip3 freeze --local > requirements
    1. echo web: python <span>app.py</span> > Procfile
    1. git add.
    1. git commit -m "initial commit"
    1. heroku git ::remote
    1. git push heroku master
    1. heroku ps:scale web=1
* In the herko app, go to settings:
    1. IP = 0.0.0.0
    1. PORT = 5000
 
* All the environment values have been saved in the env.py file

## Credits


### Content 
The product description are copied from:
* [Gym Shark](https://uk.gymshark.com/)
* [My Protein](https://www.myprotein.com/)

### Media
The product images are taken from:
* [Gym Shark](https://uk.gymshark.com/)
* [My Protein](https://www.myprotein.com/)

The backdrop image is taken from:
* [BodyBuilding estore](http://www.bodybuildingestore.com/)

The membership images are taken from:
* [Gold and Silver](http://alliancenola.org/)
* [Bronze](https://www.cmanextstep.com/)

## Acknowledgements
* [Star Reviews](https://www.youtube.com/watch?v=dPCj6Qkq13Y&feature=emb_logo)
* [JustDjango](https://www.youtube.com/watch?v=zu2PBUHMEew&t=1803s)
* [Forms](https://www.youtube.com/watch?v=3XOS_UpJirU&feature=emb_logo)

I received inspiration for this project from:  
* [Fiit Gym](https://fiit.tv/)
* [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1/tree/b5e178737596a1a1cf5be50345dc770b119918fd)

Many of the development problems have been rectifies with the guidance of 
* [StackOverflow](https://stackoverflow.com/)
* [code Institue tutors](https://courses.codeinstitute.net/login)