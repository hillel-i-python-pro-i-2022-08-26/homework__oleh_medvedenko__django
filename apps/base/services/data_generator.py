from faker import Faker

fake = Faker()


def organize_info(amount: int) -> str:
    return "".join(
        f"name: {fake.unique.user_name().lower()} | "
        f"email: {fake.unique.email().lower()} | "
        f"password: {fake.unique.password().lower()}\n"
        for _ in range(amount)
    )
