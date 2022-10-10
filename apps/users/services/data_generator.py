from faker import Faker

fake = Faker()


def generate_info() -> str:
    name = fake.unique.first_name().lower()
    email = f"{name}@{fake.unique.domain_name().lower()}"
    password = fake.unique.password().lower()
    return f"name: {name} | email: {email} | password: {password}\n"


def organize_info(amount: int) -> str:
    return "".join(f"{generate_info()}" for _ in range(amount))
