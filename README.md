# project5 - Event Management
## Distinctiveness and Complexity:
I have created an Event Management website where a user can create, read, edit, delete, and restore events.

It is distinct because it does not match the other projects in its ideas and it is more complex as:

All the events are displayed under different subheadings, namely Upcoming Events, Today's events, and Past Events, based on the date at which the events are scheduled to take place.

After commenting on an event, the comment is not displayed until the comment is authorised/approved by the owner (user who created the event) of the event.

Event owners have the option to delete their event. On deletion, the owner can request the restoration of the event by going to deleted events and checking the restore checkbox. Only the admin has the option to either approve or reject the event restoration request. On approval, the event is restored and on rejection, the restore checkbox is unchecked and the event owner can choose to send an event restoration request again by checking the restore checkbox again.

Users can also register for events. Names of the registered users can be seen only by the owner of the event under a sub-heading called registered users.

Event owners can edit all the details of their event, namely the name, date, start and end times, description, and venue of the event.

Users can add events to their favorites and can access their favorite events by clicking on the Favorite Events tab.

## Project features:
It is an Event Management website where a user can create, read, edit, delete, and restore events.

A user can:
1. Create an event
2. Comment on an event
3. Register for an event
4. Add an event to their favorites. Favorite events can be accessed by going to the Favorite Events tab.

The owners of events can (doubt):
1. Authorize/approve or reject comments on their events by going to the Authorize Comments tab. Comments are not displayed if rejected
2. See the users who have registered for their event
3. Edit all the details of their events, namely the name, date, start and end times, description, and venue of their event.
4. Delete their event
5. Send a request to restore their deleted events by going to the Deleted Events tab.

The admin can:
Approve or reject restore requests. On approval, the events are restored and on rejection, the events are not restored and the owners can send another request for restoration again if needed.

## Folders and Files I created: 
        -capstone (the app I created)  
                -static  
                        -capstone (has all the JavaScript files used in the project)    
                                -approve.js -> JavaScript file to approve restoration requests for deleted files.   
                                -authorize.js -> JavaScript file to authorize/approve or reject comments.  
                                -comment.js -> JavaScript file to comment on an event.  
                                -edit.js -> JavaScript file to edit details of an event.  
                                -favorite.js -> JavaScript file to add an event to favorites.  
                                -register.js -> JavaScript file to register for an event.  
                                -restore.js -> JavaScript file to send restoration requests for events that have been deleted.  
                        -css  
                                -capstone  
                                        -styles.css -> CSS file for the project.  
                -templates  
                        -capstone (has all the HTML templates)  
                                -approve_restore_requests.html -> HTML template for the Approve Restore Requests tab.  
                                -authorize_comments.html -> HTML template for the Authorize Comments tab.  
                                -create_event.html -> HTML template for the Create Events tab.  
                                -deleted_events.html -> HTML template for the Deleted Events tab.  
                                -event.html -> HTML template for the event specific details page.  
                                -index.html -> HTML template for the main page/All Events tab/Favorites tab.  
                                -layout.html -> HTML template that serves as the layout for the other HTML files.  
                                -login.html -> HTML template for the login tab.  
                                -register.html -> HTML template for the register tab.  
                -urls.py -> file containing all the paths for the website.  
        -project5 (the django project I created)  

## To run the application:
Clone the github repository with the project and go into the repository's directory. Then go into the web50/projects/2020/x/capstone branch and run python manage.py makemigrations capstone and python manage.py migrate to migrate changes to the database. Then run python manage.py runserver in the terminal.

## Why I created an Event Management site:
Schools usually host a lot of events. I felt that a website could help make it easier for the students to register and do other activities easily and hence, I created an Event Management site which on refinement could be used to create and manage events and help students and the school.
