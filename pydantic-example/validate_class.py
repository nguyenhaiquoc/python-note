import logging

from pydantic import BaseModel  # v2

# config basic logging
logging.basicConfig(level=logging.INFO)


class Person(BaseModel):
    name: str
    age: int


# Create an instance of the Person class
person_data = {"name": "John Doe", "age": 30}


# Validate the person dictionary
def validate_dict(person_data):
    try:
        # person = Person(**person_data)
        # validate the person object Pydantic V2
        person = Person.model_validate(person_data)
        logging.info("Person object is valid!")
        logging.info(person)
    except Exception as e:
        logging.info(f"Validation failed: {str(e)}")


# define person dataclass
class PersonData:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# write a function validate an object that have name, age attribute and validate it
def validate_object(person):
    try:
        # validate the person object Pydantic V2
        person = Person.model_validate(person)
        logging.info("Person object is valid!")
        logging.info(person)
    except Exception as e:
        logging.info(f"Validation failed: {str(e)}")


if __name__ == "__main__":
    person_data = {"name": "John Doe", "age": 30}
    validate_dict(person_data)

    person_data = {"name": "John Doe", "age": "a30"}
    validate_dict(person_data)

    # Error: Input should be a valid dictionary or instance of Person
    person = PersonData(name="John Doe", age=30)
    validate_object(person)
