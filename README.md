# Kinnect

This is the Kinnect D.R.F API.

Kinnect is a place where people alike can come together to share their love of gaming. Users can share their experiences, like and write comments, follow other users and rate user profiles. User have full customisation of their profile, have space to write about themselves and what they enjoy and add a profile picture.

This is the Backend database which was built and designed using Django Rest Frameworks.

- The deployed version of the API is [HERE](https://kinnect-api-cf0f665319fa.herokuapp.com/).
- The deployed version of the full site built in React is [HERE](https://kinnectsocial-98b2a3f8410d.herokuapp.com/).
- The frontend repository is [HERE](https://github.com/AJMCoder/kinnect_social.git).

## User Stories

Here is a link to the [User Stories](https://github.com/users/AJMCoder/projects/3).

### Admin

**User Stories:**
- As a **site admin** I can **add, edit, and delete profiles from the database** so that **users are safe from spammers or account hackers**
- As a **site admin** I can **remove posts or comments if they are not appropriate or relevant** so that **the site is enjoyable and safe for all users**
- As a **site admin** I can **see lists of all user profiles, posts, likes, and comments, followers** so that **I have an overview of all activity on the site**

### Profile Management

**User Stories:**
- As a **user** I can **sign up for an account** so that I can **make and like posts, and follow other users**
- As a **user** I can **log in and out of my account** so that I can **access the site from different devices and keep my account secure**
- As a **user** I can **add a profile picture and description** so that **I can personalise my profile**
- As a **user** I can **delete my profile** so that **my personal details are not saved if I don't want to use the site anymore**

### Post Management

**User Stories:**
- As a **user** I can **add a new post** so that **I can share my interests or achievements** 
- As a **user** I can **edit my posts** so that **I can make update if i make further progress**
- As a **user** I can **delete my posts** so that **I can remove posts made in error, or that I don't want displayed on my profile anymore**
- As a **user** I can **like and unlike other users' posts** so that **I can engage with content that I enjoy**

### Notifications System

**User Stories:**
- As a **user** I can **see if a user has liked or commented on my posts** so that **I can see how others are interacting with them**

## Testing 
Manual and validator testing is documented in my [Testing file](/Testing.md).

## Deployment

### Local Deployment
​
*Gitpod* IDE was used to write the code for this project.

To preview the project in the development environment, run the following command in the terminal:
```python3 manage.py runserver```. This will open port 8000. Click *Open Browser* when the popup window appears.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone ` `https://github.com/AJMCoder/kinnect_api.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://ajmcoder-kinnectapi-91u8eacawim.ws.codeinstitute-ide.net)

### Preparing File for Deployment
If you have not already set up Postgres for use in the deployed application, complete the following steps:

- In the terminal, type `pip3 install psycopg2-binary` and press enter.
- Install gunicorn, which will act as the web server. Type `pip3 install gunicorn` in the terminal and press enter.
- You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, which I did, then the requirements file needs to be updated using: `pip3 freeze --local > requirements.txt`:
  - In the terminal, type `pip3 freeze --local > requirements.txt`. This will create or update a file called `requirements.txt`, with a list of all the packages that Heroku will need to install to run our app.
- Create a Procfile in the root folder of your project, and add the following to the Procfile: `web: gunicorn <app_name>.wsgi:application`.

### CodeInstitute PostgreSQL Database

To host my database i used CodeInstitutes own hosting platform which can be found [here](https://dbs.ci-dbs.net/).

The instructions are as follows or you can follow the small steps on the website provided above.

- Navigate to the PostgreSQL site from Code Institute - https://dbs.ci-dbs.net/.
- Enter an email address into the input field to receive a new PostgreSQL database URL and click submit.
- Locate the link within the email account provided.
- Copy the address link to the CI PostgreSQL data ready for the next steps.

### Heroku Deployment
​
This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

To set up an account:

- Go to [heroku.com](https://www.heroku.com) to register for a free account.
- Click *Create free account*.

I used the [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) for this project, which means the Heroku command line interface (CLI) came pre-installed. Please check the [Heroku documentation](https://devcenter.heroku.com/articles/heroku-cli) for the most up-to-date installation instructions. 

To log in to the Heroku CLI:

- In the terminal, type ```heroku login -i``` and press enter.. 
- Enter your username and password in the terminal.
- If you have Multi-Factor Authentication turned on:
  - Click on Account Settings (via the avatar menu) on the Heroku Dashboard.
  - Scroll down to the API Key section and click Reveal. Copy the key.
  - Use the login command: heroku login -i
  - Enter your Heroku username.
  - Enter the API key you just copied when prompted for your password.

Deployment steps are as follows, from the Heroku dashboard:
​
- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Enter a name for your app. The app name must be unique, so you need to adjust the name until you find a name that hasn't been used.
- From the dropdown, choose the region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and add a new Config Var with the KEY set to `DATABASE_URL` and the value to the CodeInstitute PostgreSQL database URL you created above.
- I added additional Config Vars for the folLowing:
  - `ALLOWED_HOST` with the url for my deployed API (kinnect-api-cf0f665319fa.herokuapp.com).
  - `CLIENT_ORIGIN` with the url for my deployed frontend application (`not yet added`).
  - `CLIENT_ORIGIN_DEV` with the url for the development version of my frontend application (`not yet added`)
  - `CLOUDINARY_URL` copied from my [Cloudinary](https://cloudinary.com/) dashboard, because I used Cloudinary to host my static files.
  - `DISABLE_COLLECTSTATIC` to *1* because I do not need to load new static files on deployment.
  - `SECRET_KEY` which contains my secret key (also included in `env.py`).

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:
​
- At the top of the screen on Heroku, select *Deploy*.
- Next to *Deployment method* select *GitHub*, then scroll down and click *Connect to GitHub* to confirm you want to connect.
- In the *repo-name* field, search for the name of the GitHub repository to deploy, and click *Search*.
- Click *Connect* to link the GitHub repository with Heroku. 
- Scroll down to the *Manual deploy* section, and click *Deploy Branch*.
- If you like, click *Enable Automatic Deploys* in the *Automatic deploys* section to have Heroku rebuild your app every time you push a new change to GitHub.

Push this update to GitHub, and the project should now be deployed and live on Heroku.

## Credits 

### Media

- The images are all provided by [Pexels](https://www.pexels.com/).