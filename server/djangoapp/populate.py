from .models import CarMake, CarModel


def initiate() -> None:
    """Seed the database with initial car makes and models."""

    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology",
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology",
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology",
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology",
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology",
        },
    ]

    car_make_instances = []

    for data in car_make_data:
        car_make, _ = CarMake.objects.get_or_create(
            name=data["name"],
            defaults={"description": data["description"]},
        )
        car_make_instances.append(car_make)

    car_model_data = [
        {"name": "Pathfinder", "car_type": "SUV", "year": 2023, "make": 0},
        {"name": "Qashqai", "car_type": "SUV", "year": 2023, "make": 0},
        {"name": "XTRAIL", "car_type": "SUV", "year": 2023, "make": 0},
        {"name": "A-Class", "car_type": "SUV", "year": 2023, "make": 1},
        {"name": "C-Class", "car_type": "SUV", "year": 2023, "make": 1},
        {"name": "E-Class", "car_type": "SUV", "year": 2023, "make": 1},
        {"name": "A4", "car_type": "SUV", "year": 2023, "make": 2},
        {"name": "A5", "car_type": "SUV", "year": 2023, "make": 2},
        {"name": "A6", "car_type": "SUV", "year": 2023, "make": 2},
        {"name": "Sorrento", "car_type": "SUV", "year": 2023, "make": 3},
        {"name": "Carnival", "car_type": "SUV", "year": 2023, "make": 3},
        {"name": "Cerato", "car_type": "SEDAN", "year": 2023, "make": 3},
        {"name": "Corolla", "car_type": "SEDAN", "year": 2023, "make": 4},
        {"name": "Camry", "car_type": "SEDAN", "year": 2023, "make": 4},
        {"name": "Kluger", "car_type": "SUV", "year": 2023, "make": 4},
    ]

    for data in car_model_data:
        CarModel.objects.get_or_create(
            name=data["name"],
            year=data["year"],
            car_make=car_make_instances[data["make"]],
            defaults={"car_type": data["car_type"]},
        )
