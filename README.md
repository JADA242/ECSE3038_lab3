# ECSE3038_lab3
## Summary
This project implements a RESTful API that supports posting, getting, deleting, and updating of objects. 

### Functions:
POST /tank
Accepts data and creates a new object in the database. Returns a 201 status code upon successful creation.

GET /tank/{id}
Retrieves an object by its unique id. Returns a 200 status code with the object data if found, or a 404 status code if not found.

DELETE /tank/{id}
Deletes an object with the specified id. Returns a 204 status code with no content if the deletion is successful. If the object is not found, returns a 404 status code with a message indicating the object could not be found.

PATCH /tank/{id}
Expected Behavior: Updates an existing object identified by its id with the provided data. Returns a 200 status code with the updated object or a 404 status code if the object doesn't exist.

## Purpose
This code was written for the purpose of a lab for a ECSE3038 IOT course.

## Two Truths and a Lie
I graduated high school at 14.
I play for the university's volleyball team.
I like anime.
