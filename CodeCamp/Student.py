# Related to Classes and Objects
# Related to Object Functions
class Student: # doesn't need to be the same name as file
    def __init__(self, name,age,major,gpa,is_smart): # Intialization to create an Object with Attributes , must include __init__
        self.name = name # self. = this.
        self.age = age
        self.major = major
        self.gpa = gpa
        self.is_smart = is_smart

    def on_honor_roll(self): # Class Function/Method = a method can be used by the Object in the same class
        if self.gpa >=3.5:
            return True
        else:
            return False