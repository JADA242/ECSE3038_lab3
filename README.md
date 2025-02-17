# ECSE3038_lab3
## Summary
This project implements a web application with a RESTful API that supports the creation, retrieval, deletion, and updating of objects. Specifically, the DELETE endpoint allows clients to delete previously POSTed objects based on their unique identifier (id).

Functions:
POST /api/objects

Expected Behavior: Accepts data and creates a new object in the database. Returns a 201 status code upon successful creation.
GET /api/objects/{id}

Expected Behavior: Retrieves an object by its unique id. Returns a 200 status code with the object data if found, or a 404 status code if not found.
DELETE /api/objects/{id}

Expected Behavior: Deletes an object with the specified id. Returns a 204 status code with no content if the deletion is successful. If the object is not found, returns a 404 status code with a message indicating the object could not be found.
PUT /api/objects/{id}

Expected Behavior: Updates an existing object identified by its id with the provided data. Returns a 200 status code with the updated object or a 404 status code if the object doesn't exist.
Purpose
This code was written for the purpose of [insert reason here, e.g., an assignment in my web development course]. It demonstrates fundamental CRUD operations with a REST API.

Two Truths and a Lie
I have worked with both JavaScript and Python for web development.
I once met Elon Musk at a tech conference.
I am working on a gesture-to-audio smart glove project.
