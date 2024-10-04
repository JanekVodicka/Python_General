# Class
    # = blueprint
    # - class is like an object constructor
    # HODNOTY A OBJEKTY
        # OBJEKT = každá hodnota (tj. něco, co můžeš uložit do proměnné, vrátit z funkce nebo třeba seznamu)
        # V Pythonu mezi hodnotou a objektem není rozdíl
        # Obsahují jak data (informace), tak chování – instrukce nebo metody, které s těmito daty pracují

    # TŘÍDY
        # Umoznují nám logicky řadit naše data a funkce
        # V podstatě se jedná o plán pro vytvoření instancí (proměnných)!!!
        # (Instance) = nazevmodulu.nazevtridy()
        # Umožňují nám vytvořit soubor, který se bude měnit podle vstupu - příklad: pro skript pro každého zaměstnance
        # Jsou class variables, instace variables

    # Podtržítka - pro python konkrétní specifická důležitá funkce
    # __init__ is executed automatically, whenever we create the objects from this class
    # __init__ construct function
        # self - special word for python, referes to class, parameter
        # pod __init__ jsou tzv. atributes


    # Every python file that has functions or variables or classes inside is a module

    # PŘÍKLAD
        # class Class:
            # def __init__(self, další proměnné)   --- self vždy
            # def funkce(self):

        # Vytvoření konkrétního objektu
            # xxxx = Class(další proměnné)
        # Volání metody
            # xxxx.funkce()

# Fce, které jsou součástí class, are called methods
# str(), int() ... are the constructor functions

# Kdyz vytvarim treba soubor zamestnancu, tak jejich data dokazu podle tridy vytvorit
class Employee:

    def __init__(self, first, last, pay):   # init metoda, self=konvence, pouzivat
        self.first = first
        self.last = last
        self.pay = pay

        self.email = first + '.' + last + '@seznam.cz'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# Objects
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('User', 'Test', 6000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())

# CREATE CLASS
# vše pod class je class body
class User:

    # Constructor logic
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}.")

# CREATE OBJECT and saving it to variable
    # Variable = Object
app_user_1 = User("nn@nn.com", "Jan Vodicka", "pwd1", "DevOps Engineer")
app_user_1.get_user_info()
app_user_1.change_job("DevOps trainer")
app_user_1.get_user_info()

app_user:2 = User("jj@jj.com", "James Bond", "psw2", "Agent")
