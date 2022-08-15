# CS-340 README

## About the Project/Project Title
The project is the Animal Shelter Data Repository Project. It is designed to provide access to create, read, update, and delete records in the Animal Shelter persistence layer.

## Motivation
This project will make it easier to communicate with the persistence layer of an Animal Shelter application by providing a wrapper around the implementation details and simply give access to a specific set of methods for required functionality.

## Screen Cast
[ScreenCast](https://www.screencast.com/t/CAfGVg3Y)

## Getting Started
To get a local copy up and running, follow the simple installation steps below, and then run a script that initializes the repository and makes repository method calls according to the code examples provided in the usage section.

The Create and Read methods of the Python module were created by using the PyMongo documentation and gratuitous use of the print function to log. The challenge that was encountered was where I attempted to access an object in the cursor by using the array index accessor. Once I realized that the for loop was the way to access the objects in the cursor, then it was smooth sailing.

## Installation
You must have python and pip installed to use the application.
Set up mongo db locally with a Database called AAC, a collection called animals, and a user called aacuser with the password aacuser at localhost:27017.
To connect to an exiting database with an existing user, update the MongoClient and username and password portions of the repository code.
pip install pymongo
Note: do not pip install bson. Pymongo relies on a specific version that it will install itself.

## Usage

## Code Example
- Initialize the repo.
- `repo = AnimalShelterRepository()`

### Create a record. 
- Records should consist of a dictionary of key/value pairs.
- Returns True on success.
- `repo.create({ "id": 99, "animal_type": "Pterodactyl" })`

### Query for records the animal_type of Pterodactyl.
- Any key/value pair can be used.
- Get the second page of 5 records per page.
- `page` and `page_size` default to 1 and 10 respectively.
- `query_result = repo.query({ "animal_type": "Pterodactyl" }, 2, 5)`

### Get a record by Id.
- Returns the document if found.
- `repo.get(ObjectId('62dc6f85328393eb83431455'))`

### Delete a record by Id
- Returns true if the record was deleted.
- `repo.delete(ObjectId('62dc6f85328393eb83431455'))`

## Tests
Manual Tests are executed in the Test.ipynb file.

## Screenshots
![test screenshot](./screenshot.png)

## Tools
- Visual Studio Code – VS Code is a lightweight code editor with support for both Python and Jupyter notebooks.
- Jupyter VS Code Extension – VS Code extension allowing easy to use access to Jupyter notebook functionality.
- Mongo DB – Required by the assignment.
- PyMongo – Required by the assignment.
- Dash Leaflet - Used by the map widget.
- Plotly - Used to create the Pie chart.
- Numpy - Used for data manipulation to get the pie chart to appear correctly.
- Pandas - Used for data manipulation.

## Contact
Your name: Mark Holden
