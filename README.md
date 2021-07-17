# project5 - Event Management
## Distinctiveness and Complexity:
This is an application for managing Events where a user can create, read, edit, delete,
and restore events. An Event is an entity that occurs over a period in a day. Apart from
the other static attributes like Name, Description etc., it has a dynamic a dynamic
attribute viz. Status, which is calculated on the fly based on the Event data and current
date. The three values of Status are as follows:
1. Upcoming Event – Events with their date attribute in future.
2. Today’s Evens – Events with their date attribute in future.
3. Past Event – Events with their date attribute in future.

It is distinct compared to other projects in the course along the following lines:
1. Dynamic attribute - Events are grouped by the dynamic attribute viz. Status
2. Approval process - Comments posted on an Event will have to be
authorized/approved by the owner of the Event before they get published.
3. Soft delete and restoration - Event owners have the option to delete the Events
that they own upon which these will not be visible to other users but is visible to
the owner identified by the Event name and as deleted. However, this is a soft
deletion, and the owner can request the restoration of the event that goes to the
Admin of the site who has the option to either approve or reject the event
restoration request.
4. Constraints on Read - Users can also register for certain events of their liking.
Only the owner of the Event will have the privilege to see the list of users
registered on the Event he is the owner for.
5. Constraints on Edit – Only Event owners will have the privileges to edit all the details of the
Events that they own.
6. Filter based on my favorites - Users can add events to their favorites and can
access their favorite events by clicking on the Favorite Events tab.

## Project features:
It is an Event Management website where users can register, manage Events and work
on the Events collaboratively amongst users with the required privileges.
The various features of the application can be accessed by users based on their Roles.
A person has to register on the application through a self serving form to be able to log
into the application and work on it. Following are the Roles in the Application.
1. Application Admin
2. Event Owner
3. Event Participant

a. Event Owner – A user can Create an event and be the designated owner of the
Event. The Event Owner will have the following privileges.
1. Authorize/approve or reject comments on their events by going to the
Authorize Comments tab. Comments are not displayed if rejected
2. See the users who have registered for their event
3. Edit all the details of their events, namely the name, date, start and end
times, description, and venue of their event.
4. Delete their event
5. Send a request to restore their deleted events by going to the Deleted
Events tab.

b. Application Admin - Admin can Accept/Reject a request for restoration of a
deleted Event. The events are restored on Accept and are not restored on
Rejection. Also, on Rejection, the owners can send another request for
restoration.

c. Event Participants - Users can Register on an Event of their choice and become
Event Participants. Event participants will be able to
1. View the Event details as also the activities/comments on it.
2. Post comments on the Event
3. Mark any Event as favourite
4. Get a filtered list of Favorite events by going to the Favorite Events tab.

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
The schools usually host a lot of events. I felt that automating the process of Event
Management could help the school staff to manage these events much more effectively
and efficiently while the students would find it much less hassle free to track the Events
they are a part of. This application could be enhanced and refined further to suit
customized requirements from schools and help them become much more productive
on Event Management.
