for reviews: https://www.youtube.com/watch?v=dPCj6Qkq13Y&feature=emb_logo


# VirtualGym


## UX



Below are some user stories :
1. __User wants to :__  
    
      
2. __User wants to :__  
  


__During the early stages, a rough__ [wireframe](static/pdf/ .pdf) __was made using balsamiq__  


## Features

### Existing Features:
Navigation: allows the user to choose between what they want to acheive by clicking on the tab (code in: base.html).

Buy products: allows users to add a recipe by filling out the add recipe form (code in: new_recipe.html)

sort: allows users to choose which recipe they want to view, edit and/or delete by choosing the cuisine from a drop down

subscribe: allows the users to view the entire recipe by clicking on the name of the recipe

activity board: allows the users to view some charts

login/signup: allows the users to login to an account/create an account to manipulate values saved in the database by filling out the username and password

### Features Left to Implement
* 
* 
* 
* 
* 
*  


## Technologies Used

**HTML:** Hypertext Markup Language (HTML) was used to create the webpage. 

**CSS:** Cascading Style Sheets (CSS) was used to add customised styling to the webpage.

**JavaScript:**  JavaScript enables interactive web pages and is an essential part of web applications. It was used to add interactive functionality to the webpage

**Python:** Python was used for the server side web development. Also to connect to the database and perform various operations of its data.

**Django:** [Django](https://) 

**Bootstrap:** [Bootstrap](https://) was 
the database used to store the data for this web application. 
It is a document database, which means it stores data in JSON-like documents.

**Balsamiq:** [Balsamiq](https://balsamiq.com/) was used to create wireframe. It was used in the initial stages of the project visualisation. It was used to put the idea of a page decide the layout and flow of the project. 

**JQuery:** [JQuery](https://jquery.com/) was used to simplify DOM manipulation.

## Testing

Manual testing was done on all the forms of this project

**Register form:**  
Try to submit the empty form and verify that an error message about the required fields appears.  
Try to submit the form with an invalid url format and verify that a relevant error message appears.  
Try to submit the form with an invalid title and verify that an error message about the invalid format appears.  
Try to submit the form with an invalid calories and verify that an error message about the invalid format appears.  
Try to submit the form with all inputs valid and verify that the values get stored in the database. 

**Login form:**   

**Checkout form:**  

**review modal**

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
* 
* [Cook With Manali](https://www.cookwithmanali.com/)  

### Media
The recipe images are taken from:
* [Gym Shark](https://uk.gymshark.com/)
* [My Protein](https://www.myprotein.com/)

The backdrop image is taken from:
* [BodyBuilding estore](http://www.bodybuildingestore.com/)

The membership images are taken from:
* [Gold and Silver](http://alliancenola.org/)
* [Bronze](https://www.cmanextstep.com/)

## Acknowledgements
* [Star Reviews]()
* [JustDjango]()

I received inspiration for this project from:  
* [Fiit Gym](https://fiit.tv/)
* [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1/tree/b5e178737596a1a1cf5be50345dc770b119918fd)

Many of the development problems have been rectifies with the guidance of 
* [StackOverflow](https://stackoverflow.com/)
* [code Institue tutors](https://courses.codeinstitute.net/login)