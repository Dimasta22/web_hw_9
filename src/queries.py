from sqlalchemy import and_


from src.session_db import session
from src.models import User


def add_contact(first_name, last_name, email, address, phone):
    user = User(first_name=first_name, last_name=last_name, email=email, address=address, phone=phone)
    session.add(user)
    session.commit()
    session.close()
    return user


def update_contact(first_name, last_name, email, address, phone):
    user = session.query(User).filter(and_(User.first_name == first_name, User.last_name == last_name))
    user.update({'email': email, 'address': address, 'phone': phone})
    session.commit()
    session.close()
    return user.one()


def delete_contact(first_name, last_name):
    user = session.query(User).filter(and_(User.first_name == first_name, User.last_name == last_name)).delete()
    session.commit()
    session.close()
    return user


def all_contact():
    contacts = session.query(User).all()
    return contacts
