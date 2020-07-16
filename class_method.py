class Employee:

    num_of_emps = 0  # class variable
    raise_amt = 1.05 # class variable
    # constructor /Special method
    def __init__(self, fname, lname , pay):

        self.firstname = fname

        self.lastname = lname

        self.salary = pay

        self.email = self.firstname + self.lastname + '@company.com'

        Employee.num_of_emps += 1  # use both operator together otherwise shows error

    # Instance /Regular method
    def fullname(self):

        return '{}' '{}'.format(self.firstname, self.lastname)

    # Instance /Regular method
    def apply_raise(self):

        self.salary = int(self.salary * self.raise_amt)

        return self.salary

    @classmethod                 # use classmethod decorator
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount


    @classmethod
    def from_string(cls, emp_str):   # class method as a alternative constructor
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)

    @staticmethod      # use static method decorator
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

    def __repr__(self):

      return self.firstname +'---------------->' +self.lastname

var = Employee("Amit","Saxena",700)

print(var)




