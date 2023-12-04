"""
This module split email.

Author: Maryam Alavi
"""


def main():
    """this is for say welcome"""
    print("welcome to the email spliter")
    print("")

    email_input = input("input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("username :", username)
    print("domain :", domain)
    print("extension:", extension)


main()
