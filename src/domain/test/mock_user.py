from faker import Faker

from src.domain.models import Users

faker = Faker()


def mock_users() -> Users:
    """Mocking a new User"""

    return Users(
        id=faker.random_number(digits=2), name=faker.name(), password=faker.password()
    )
