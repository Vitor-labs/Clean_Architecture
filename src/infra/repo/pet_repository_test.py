from faker import Faker

from src.infra.entities.pets import PetsTypes
from src.infra.entities import Pets as PetsModel
from src.infra.config import DBConnectionManager
from .pets_repository import PetRepository

faker = Faker()
pet_repo = PetRepository()
conn = DBConnectionManager()


def test_insert_pet():
    "Should inser a pet in Pets table and return it"

    name = faker.name()
    specie = "FISH"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    new_pet = pet_repo.insert_pet(name, age, specie, user_id)

    engine = conn.get_engine()
    query = engine.execute(
        "SELECT * FROM pets WHERE id={}".format(new_pet.id)
    ).fetchone()

    assert new_pet.id == query.id
    assert new_pet.name == query.name
    assert new_pet.age == query.age
    assert new_pet.specie == query.specie
    assert new_pet.user_id == query.user_id

    engine.execute("DELETE FROM pets WHERE id={}".format(new_pet.id))


def test_select_pet():
    """Should select a pet in Pets table and comparte it"""

    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "DOG"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    specie_mock = PetsTypes("DOG")
    data = PetsModel(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    engine = conn.get_engine()
    engine.execute(
        "INSERT INTO pets (id,name,specie,age,user_id) VALUES ('{}','{}','{}','{}','{}')".format(
            pet_id, name, specie, age, user_id
        )
    )

    query1 = pet_repo.select_pet(id=pet_id)
    #    query2 = pet_repo.select_pet(user_id=user_id)
    #    query3 = pet_repo.select_pet(id=pet_id, user_id=user_id)

    engine.execute("DELETE FROM pets WHERE id={}".format(pet_id))

    assert data.id == query1.id
    assert data.name == query1.name
    assert data.age == query1.age
    assert data.specie.value == query1.specie.value
    assert data.user_id == query1.user_id
