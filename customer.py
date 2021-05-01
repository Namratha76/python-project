class Customer:
    def __init__(self, firstName = None, lastName = None, age = None, phone = None):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.phone = phone
    
    def setFirstName(self, firstName):
        self.firstName = firstName

    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getLastName(self):
        return self.lastName

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone