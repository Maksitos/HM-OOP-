class Employee:
    def __init__(self, name, surname, mail, phone, zp_per_day):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.phone = phone
        self.zp_per_day = zp_per_day

    def work(self):
        return 'I come to the office'

    def check_salary(self, days_worked):
        return days_worked * self.zp_per_day


class Recruiter(Employee):
    def work(self):
        return 'I come to the office and start hiring'


class Programmer(Employee):
    def work(self):
        return 'I come to the office and start coding'
