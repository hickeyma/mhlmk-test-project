"""
Entry point to run the package
"""

from test_project.dog import dog


def main():
    """
    main function
    """
    my_dog = dog.Dog()
    print(f"{my_dog.what_am_i()}")


if __name__ == "__main__":
    main()
