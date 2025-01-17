# AirBnB Clone - The Console

## Project Overview

The goal of this project is to deploy on a server a simple copy of the AirBnB website. 

## Features

### Console

The console is a command interpreter to manage your AirBnB objects. It allows you to:

- Create a new object (e.g., a new User or a new Place)
- Retrieve an object from a file, a database, etc.
- Do operations on objects (e.g., count, compute stats)
- Update attributes of an object
- Destroy an object

## Project Tasks

Each task is linked and will help you to:

1. **BaseModel**: Put in place a parent class (called `BaseModel`) to take care of the initialization, serialization, and deserialization of your future instances.
2. **Serialization/Deserialization**: Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
3. **Class Creation**: Create all classes used for AirBnB (User, State, City, Place…) that inherit from `BaseModel`.
4. **Storage Engine**: Create the first abstracted storage engine of the project: File storage.
5. **Unit Tests**: Create all unit tests to validate all our classes and storage engine.

## Getting Started

To get started with the console, clone the repository and run the console script:

```bash
git clone https://github.com/lilalajemima/alu-AirBnB_clone.git
cd alu-AirBnB_clone
./console.py
```

## Usage

Here are some example commands you can run in the console:

- Create a new User:
    ```bash
    (hbnb) create User
    ```

- Show an object:
    ```bash
    (hbnb) show User <user_id>
    ```

- Destroy an object:
    ```bash
    (hbnb) destroy User <user_id>
    ```

- Update an object:
    ```bash
    (hbnb) update User <user_id> <attribute_name> <attribute_value>
    ```

## Authors

- Your Name - [GitHub Profile](https://github.com/yourusername)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
