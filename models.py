from datetime import datetime
from db_manager import Database

class Expence(object):
    """ 
        A model class for expences
    """

    def __init__(self, amount, category, date_time , description = "" ,  ):
        self.amount = amount
        self.category = category
        self.date_time = date_time
        self.description = description
    
    def get_db_date(self):
        return self.date_time.strftime('%d %b %Y')

    def save(self):
        """
        Save into database
        """
        db = Database()
        db.save_expence(self)

class Income(object):
    """ 
        A model class for incomes
    """

    def __init__(self, amount, source ,date_time , description = "" ):
        self.amount = amount
        self.source = source
        self.date_time = date_time
        self.description = description

    def get_db_date(self):
        return self.date_time.strftime('%d %b %Y')

    def save(self):
        """
        Save into database
        """
        db = Database()
        db.save_income(self)