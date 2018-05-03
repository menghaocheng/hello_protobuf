import protobuf.addressbook_pb2 as addressbook_pb2


def ListPeople(address_book):
  for person in address_book.people:
    print("Person ID:", person.id)
    print("  Name:", person.name)
    print("  E-mail address:", person.email)

    for phone_number in person.phones:
      if phone_number.type == addressbook_pb2.Person.MOBILE:
        print("  Mobile phone #: ")
      elif phone_number.type == addressbook_pb2.Person.HOME:
        print("  Home phone #: ")
      elif phone_number.type == addressbook_pb2.Person.WORK:
        print("  Work phone #: ")
      print(phone_number.number)


def read_test():
    address_book = addressbook_pb2.AddressBook()
    address_book_file = "./data/addressbook.txt"

    f = open(address_book_file, "rb")
    address_book.ParseFromString(f.read())
    f.close()

    ListPeople(address_book)


if __name__ == "__main__":
    read_test()
