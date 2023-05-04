# class Student:
# name = "Winfrida"
#     age = 21
#     school = "Akirachix"
#     nationality = "Kenyan"
class Student:    
    school = "Akirachix"
    def __init__(self,name,age,nationality):
       self.name = name
       self.age = age
       self.nationality = nationality
    def greet__student(self):
        return f"Hello{self.name},welcome to {self.school} proud{self.nationality}"
    #  Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
    #          - show_full_name
    #          - year_of_birth
    #          - show_initials
    class Student:
        name = "Winfrida"
        age = 21
        school = "Akirachix"
        nationality = "Kenyan"
        first_name = "Winfrida"
        last_name = "Obinyo"
        country = "Kenya"
        year_of_birth = 2001
        
    class Student:
        school ="Akirachix"
    def __init__(self,name,age,nationality,first_name,last_name,country,yearofbirth):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.first_name =first_name
        self.last_name = last_name
        self.country = country
        self.age = age
        self.yearofbirth=yearofbirth
    def greet__student(self):
        return f"Hello{self.name},welcome to {self.school} proud{self.nationality}"
    def show_full_name(self):
        return f"Hello {self.first_name}{self.last_name}"
    def year_of_birth(self):
        return f"Hello{self.age}"
    def show_initials(self):
        return f"Hello {self.first_name[0].Upper()},{self.last_name[0].upper()}"
    