from src.queries import add_contact, all_contact, update_contact, delete_contact


if __name__ == '__main__':

    first_name = 'Dima'
    last_name = 'Serdiuk'
    email = 'hguolkkmn@gmail.com'
    address = 'Bud 4, 65'
    phone = '+380(67)333-33-44'
    add_contact(first_name, last_name, email, address, phone)

    contacts = all_contact()

    for contact in contacts:
        print(f'{contact.first_name} {contact.last_name}; {contact.email}; '
              f'{contact.address}; {contact.phone}')

    first_name = 'Dima'
    last_name = 'Serdiuk'
    email = 'hguolkkmn@mail.com'
    address = 'Bud 4, 89'
    phone = '+380(69)333-33-44'

    new_contact = update_contact(first_name, last_name, email, address, phone)
    print(f'{new_contact.first_name} {new_contact.last_name}; {new_contact.email}; '
          f'{new_contact.address}; {new_contact.phone}')

    remove_user = delete_contact(first_name, last_name)
    print(remove_user)


