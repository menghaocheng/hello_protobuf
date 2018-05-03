from protobuf import addressbook_pb2


def PromptForAddress(person):
    person.id = 1
    person.name = "mc.meng"
    person.email = "menghaocheng@qq.com"
    phone_number = person.phones.add()
    phone_number.number = "18565772445"
    phone_number.type = addressbook_pb2.Person.MOBILE


def write_test():

    address_book = addressbook_pb2.AddressBook()

    address_book_file = "./data/addressbook.txt"

    try:
      f = open(address_book_file, "rb")
      address_book.ParseFromString(f.read())
      f.close()
    except IOError:
      print(address_book_file + ": Could not open file.  Creating a new one.")

    PromptForAddress(address_book.people.add())

    f = open(address_book_file, "wb")
    f.write(address_book.SerializeToString())
    f.close()


if __name__ == "__main__":
    write_test()
