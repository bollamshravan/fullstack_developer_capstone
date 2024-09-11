"""
Module to populate the database with CarMake and CarModel instances.
"""

from .models import CarMake, CarModel

def populate_database():
    """
    Function to populate the database with CarMake and CarModel instances.
    """
    car_make_data = [
        {"name": "Nissan", "description": "Japanese car manufacturer"},
        {"name": "Mercedes-Benz", "description": "German car manufacturer"},
        {"name": "Audi", "description": "German car manufacturer"},
        {"name": "Kia", "description": "South Korean car manufacturer"},
        {"name": "Toyota", "description": "Japanese car manufacturer"},
        # Add more CarMake instances as needed
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=data['name'], description=data['description'])
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4]},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year']
        )

# Call the function to populate the database
populate_database()
