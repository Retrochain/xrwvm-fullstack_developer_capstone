from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    """
    Represents a car manufacturer (e.g., Toyota, Ford, BMW).
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    country = models.CharField(max_length=100, blank=True)
    founded_year = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class CarModel(models.Model):
    """
    Represents a specific car model belonging to a CarMake.
    """

    CAR_TYPE_SEDAN = "SEDAN"
    CAR_TYPE_SUV = "SUV"
    CAR_TYPE_WAGON = "WAGON"

    CAR_TYPES = [
        (CAR_TYPE_SEDAN, "Sedan"),
        (CAR_TYPE_SUV, "SUV"),
        (CAR_TYPE_WAGON, "Wagon"),
    ]

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name="models",
    )

    name = models.CharField(max_length=100)

    car_type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default=CAR_TYPE_SUV,
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023),
        ]
    )

    class Meta:
        ordering = ["-year", "name"]
        unique_together = ("car_make", "name", "year")

    def __str__(self) -> str:
        return f"{self.car_make.name} {self.name} ({self.year})"
