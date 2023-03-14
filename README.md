# IOttaRent (Django-Python-Web-Application)

# Project Description
This full-stack web application is built using Django, one of the most popular web frameworks in the Python ecosystem. 
The objective of the project is to provide comprehensive information about rentals in Ottawa, catering to the needs of tenants, landlords, and realtors alike.

As a tenant, you can use this application to search for properties that meet your specific requirements, 
such as location, budget, number of bedrooms, and amenities. You can also view pictures of the property, 
see its availability status, and contact the landlord or realtor for further details.

If you're a landlord or realtor, you can use this application to list your properties and reach a wider audience of potential tenants.
You can also provide your professional suggestions and tips to help tenants make informed decisions about renting your properties.

This project is a testament to the my proficiency in Python and Django, showcasing the ability to develop a full-stack web application from scratch. 
It demonstrates expertise in handling databases and implementing front-end user interfaces using modern web technologies.

Overall, this application aims to simplify the rental process in Ottawa, making it easier for both tenants and landlords to find their ideal rental properties.

# Table of Contents
a. Web Application Interface


## a. Web Application Interface

### 1. Home Page

At the top of the home page, you will find a navigation bar that enables easy movement to various sections of the website. Users have the option to either login or sign-up to access the features of the site or navigate to their desired pages.

The body of the home page provides a detailed description of the goals and objectives that we aim to achieve with this web application. We strive to create a user-friendly platform that allows individuals to easily rent their desired properties without any hassle.

In addition to the navigation bar and body content, the footer at the end of the webpage provides essential information about IOttaRent, including contact details and links to relevant social media platforms.

![home page](/project_demo_image/home_page_1.png)
![home page](/project_demo_image/home_page_2.png)
![home page](/project_demo_image/home_page_3.png)
![home page](/project_demo_image/home_page_4.png)

### 2. About Page

This webpage provides information about the mission, services, responsibility, and technologies used. 

![About Page](/project_demo_image/about1.png)
![About Page](/project_demo_image/about2.png)
![About Page](/project_demo_image/about3.png)

### 3. Sign-up Selection Page

This webpage allows users to choose their type of account based on their identity, either a user/landlord or a realtor. 

![Select Account Type Page](/project_demo_image/select.png)

### 4. Sign-up Page for User/ Landlord

This webpage allows User/ Landlord to register an account in IOttawa. 

User must provide their username, password, avatar, bio, and phone number.

Backend logic checks whether their input fulfil the requirement of each filed, if it does not, a flash message appears.

![Sign-up Page for User](/project_demo_image/user1.png)
![Sign-up Page for User](/project_demo_image/user2.png)


### 5. Sign-up Page for Realtors

This webpage allows realtors to register an account in IOttawa. 

It is very similar to the sign-up page for normal user, the only difference is that realtor may choose to provide their company information.

![Sign-up Page for Realtor](/project_demo_image/realtor1.png)
![Sign-up Page for Realtor](/project_demo_image/realtor2.png)


### 6. Login Page

This webpage allows users to login using their userid and password.

If they do not have an account yet, they can click the sign-up link at the bottom of the form, which redirects them to the sign up page.

![Login Page](/project_demo_image/login_form.png)

### 7. Listing page

After successfully logging in or registering their account, users will be redirected to the current listing page.

On this page, all available rentals on the website will be displayed with brief information. Users can utilize the search and filter functions to find rentals that suit their needs. They can also filter rental results by categories, such as 1-bedroom apartments or basements. In the third column of the webpage, some featured realtors are displayed with relevant information, enabling users to seek professional advice from realtors.

Each page will be showing maximum 5 listings, and the listing page paginates after maximum number of listings is reached.

![Listing Page](/project_demo_image/listing1.png)
![Listing Page](/project_demo_image/listing2.png)
![Listing Page](/project_demo_image/listing3.png)


- demostration of the filter function

![Listing Page](/project_demo_image/demo_filter.png)


### 8. Individual Rental Advertisement Page

Once the user clicked on the 'View Details' button of Listing page, he/ she will be redirected to the Rental Advertisement Detail Page.

In this page, user can view important information about the specific rental, including description, address, amenities included, rent, availability, category, and landlord contact information.

If the user is interested in the rental, he/she can send an enquiry message to the landlord or realtors for further information, or even schedule a visiting tour as they wish.

![Rental Advertisement Detail Page](/project_demo_image/unit1.png)
![Rental Advertisement Detail Page](/project_demo_image/unit2.png)


### 9. Individual Profile Page

Each user has his/her corresponding profile page. 
The profile page will display user's personal information, including their profile picture, username, bio, and contact information. 
If a different user wants to contact a specific user, they can utilise the message function at the bottom of the profile page.

On the right side of the webpage, rental advertisement posted by the specific user are shown.

![Individual Profile Page](/project_demo_image/profile1.png)
![Individual Profile Page](/project_demo_image/profile2.png)
![Individual Profile Page](/project_demo_image/profile3.png)

### 10. Profile Update Form Page

If user wish to update their profile or account information, they can click on the 'Edit Profile' button. Then, they will be redirected to a profile update form, 
where user can choose to update their personal information.

![Individual Profile Page](/project_demo_image/update_profile1.png)
![Individual Profile Page](/project_demo_image/update_profile2.png)


### 11. Message Thread Page

Each user can see his/her conversation with other users in the message thread page.
The lastest message between 2 users will be displayed as well as the timestamp.

![Individual Profile Page](/project_demo_image/thread.png)

























