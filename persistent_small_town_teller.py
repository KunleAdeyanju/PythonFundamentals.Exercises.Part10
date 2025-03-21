import small_town_teller
import json
import pickle
import os

class PersistenceUtils():

    def __init__(self):
        pass

    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, "wb") as handler:
            pickle.dump(data, handler)
    

    @staticmethod
    def load_pickle(file_path):
        with open(file_path, "rb") as handler:
            data = pickle.load(handler)
        return data


class Bank2(small_town_teller.Bank, PersistenceUtils):
    
    def save_data(self):
        self.write_pickle("/Users/kunle/Projects/PythonFundamentals.Exercises.Part10/customer.pickle", self.customer)
        self.write_pickle("/Users/kunle/Projects/PythonFundamentals.Exercises.Part10/accounts.pickle", self.account)

    def load_data(self):
        self.customer = self.load_pickle("/Users/kunle/Projects/PythonFundamentals.Exercises.Part10/customer.pickle")
        self.account = self.load_pickle("/Users/kunle/Projects/PythonFundamentals.Exercises.Part10/accounts.pickle")