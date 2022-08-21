# Module 8 Journal
### How do you write programs that are maintainable, readable, and adaptable? 
At work, I write programs that are maintainable, readable, and adaptable by writing self-documenting code using a test-driven approach. To make the code as adaptable as possible, I endeavor to extract code out into smaller and smaller methods until methods are around the ~4 line mark. From an architectural perspective, one of the previous companies that I worked for was heavily influenced by onion architecture, and I strive to apply that type of architecture and put use domain-driven design to make the code make sense.

### Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way?
In my opinion, the repository is actually pretty gross, because there are a ton or checks of different random things in the code the way data is returned from the cursor is nasty.

### How else could you use this CRUD Python module in the future?
I would not use the CRUD Python module in the future unless it were required by an assignment.

### How do you approach a problem as a computer scientist?
I endeavor to approach every problem by following the Elon Musk Five Step Engineering Process:
1. Make your requirements less dumb (Requirements must come with a Name, not a department).
2. Try hard to delete the part or process (If you aren't adding back 10% of the time, you aren't deleting enough).
3. Simplify or optimize (Most common error of a smart engineer is to optimize a thing that does not exist).
4. Accelerate cycle time (Not until after you have done all the others - if you are digging your grave, don't dig it faster, stop digging!).
5. Automate.

### Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses?
My approach to this project was the same as my approach to software development at work - SOLID Principles, Clean Code, and DRY. Within the limitations of the assignments, I endeavor to follow that approach.

### What techniques or strategies would you use in the future to create databases to meet other client requests?
The first technique that I would employ before creating any database to meet a client request is to think critically about whether a database is actually the right solution for the client's requirements. Client's may think they need a database, but if experience is any indication, clients do not always know what the best solution is to fulfill the actual need that they are presenting. Assuming the client's requirements do indicate the necessity of a database, then because of my heavy SQL background, I would gravitate towards an SQL database unless there were contraindications. If the client simply needed fast lookup on documents with fuzzy search, Elasticsearch might be the right answer. If the client needed to look up records based on their relationships with one another, then a relational database is going to be the answer.

### What do computer scientists do, and why does it matter?
Computer scientist covers a very broad range of occupations. Some occupations held by computer scientists may be theoretical research on computer hardware or software, or they may be cryptographers who work to develop or crack the latest encryption schemes. It may refer to software engineers, who basically run the entire world. Software Engineering matters because pretty much everything runs on software at some level, and software engineers are the ones that make the software.

### How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
In my option, creating dashboards is not be something that a software engineer should be spending their time doing. What the software engineer should provide is the functionality to the end user to create their own custom dashboard. If I had done this work for a company, I should have been fired immediately.


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
