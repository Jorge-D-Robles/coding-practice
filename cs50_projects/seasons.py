from datetime import date, datetime, timedelta
import sys
import inflect
p = inflect.engine()


def main():
    today = date.today()
    birthday = get_birthday()
    time_to_birthday = abs(birthday - today)
    minutes = time_to_birthday.days * 1440
    print(minutes)
    words = p.number_to_words(minutes).capitalize()
    print(words)


def get_birthday():
    try:
        birthday = input("Date of Birth: ")
        birthday = date.fromisoformat(birthday)

    except ValueError:
        sys.exit("Please try again. Bye.")
    return birthday


if __name__ == "__main__":
    main()
