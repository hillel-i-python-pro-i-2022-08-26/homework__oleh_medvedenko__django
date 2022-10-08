from faker import Faker

fake = Faker()


def username_generator():
    return fake.unique.user_name()


def password_generator():
    return fake.unique.password()


def email_generator():
    return fake.unique.email()


def organize_info(amount: int):
    return "".join(
        f"name: {fake.unique.user_name()} | " f"email: {fake.unique.email()} | " f"password: {fake.unique.password()}\n"
        for _ in range(amount)
    )
