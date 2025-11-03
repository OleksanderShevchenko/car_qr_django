# cqs_django/django_car_service/cars/models.py
from django.db import models
from django.conf import settings


class Car(models.Model):
    """
    Модель Автомобіля.
    "Переклад" вашої SQLAlchemy Car model.
    """

    # 1. id: Mapped[int] = mapped_column(primary_key=True)
    #    Django додає 'id = models.AutoField(primary_key=True)' АВТОМАТИЧНО.

    # 2. license_plate: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    license_plate = models.CharField(max_length=20, unique=True, db_index=True)

    # 3. brand: Mapped[str] = mapped_column(String(50))
    brand = models.CharField(max_length=50)

    # 4. model: Mapped[str] = mapped_column(String(50))
    model = models.CharField(max_length=50)

    # 5. owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    #    owner: Mapped["User"] = relationship(back_populates="cars")
    #
    #    Django об'єднує ці два рядки в одне поле ForeignKey:
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Найкращий спосіб посилатися на User
        on_delete=models.CASCADE,  # Що робити, якщо User видалений? (CASCADE = видалити авто)

        # 'related_name="cars"' - це аналог вашого 'back_populates="cars"'.
        # Це дозволить нам писати 'user.cars.all()'
        related_name="cars"
    )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"