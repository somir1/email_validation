from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email():

    def __init__(self, data):
        self.id = data['id']
        self.email_ad = data['email_ad']
        self.created_at = data['created_at']

    @classmethod
    def show(cls):
        query = "SELECT * FROM email"
        results = connectToMySQL('email_schema').query_db(query)

        emails = []
        for item in results:
            new_email = Email(item)
            emails.append(new_email)

        return emails

    @classmethod
    def make(cls, data):
        query = "INSERT INTO email(email_ad) VALUES (%(email_ad)s);"

        return connectToMySQL('email_schema').query_db(query, data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['email_ad']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid




