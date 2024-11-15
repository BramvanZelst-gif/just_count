import click

@click.command()
@click.argument(f"square {x}")
# @click.option(
#     "-",
# )




def square(x):
    return x**2


if __name__ == "__main__":
    print(f"The square of {x} is {square(x)}")
