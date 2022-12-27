from faker import Faker

from src.domain.models import Pets

faker = Faker()


def mock_pets() -> Pets:
    """Mocking a new Pet
    Returns:
        Pets: a new pet
    """
    return Pets(
        id=faker.random_number(digits=5),
        name=faker.name(),
        specie=faker.name(),
        age=faker.random_number(digits=1),
        user_id=faker.random_number(digits=4),
    )
