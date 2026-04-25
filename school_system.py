"""
+----------------------+----------------------+----------------------+
|        Aluno         |      Professor       |      Estagiario      |
+----------------------+----------------------+----------------------+
| RG                   | Nome                 | Endereco             |
| Endereco             | Data de Nascimento   | Valor Bolsa          |
| Data de Ingresso     | Codigo Funcionario   | Data Inicio Estagio  |
| Codigo Aluno         | CPF                  | RG                   |
| Nome                 | Disciplinas          | Codigo Estagiario    |
| Curso                | Endereco             | Data de Nascimento   |
| Data de Nascimento   | Data de Admissao     | Codigo Aluno         |
| Semestre             | RG                   | CPF                  |
| Valor da Mensalidade |                      | Nome                 |
| CPF                  |                      |                      |
+----------------------+----------------------+----------------------+
"""

'''
Pessoa
│
├── attributes:
│   - nome
│   - rg
│   - cpf
│   - endereco
│   - data_nascimento
│
├── Aluno
│   - codigo_aluno
│   - data_ingresso
│   - curso
│   - semestre
│   - valor_mensalidade
│
│   └── Estagiario
│       - codigo_estagiario
│       - data_inicio_estagio
│       - valor_bolsa
│
└── Professor
    - codigo_funcionario
    - disciplinas
    - data_admissao

- Organizar as classes criando uma Superclasse e utilizando os conceitos de herança visando o aproveitamento e otimização de código.
- Fazer um programa baseado nas classes dadas, no qual seja possível se cadastrar os alunos, professores e estagiários, e possa se listar cada um deles em separado, ou todos juntos.
- Criar código seqüencial para os códigos de aluno, estagiário e professor.
- Dividir o programa em diversos métodos utilizando o reaproveitamento de código;
'''

# school management
class School:
    
    def __init__(self):
        self.student_count = 0
        self.professor_count = 0
        self.intern_count = 0

        self.students = []
        self.professors = []
        self.interns = []

    def register_student(self, student : Student):
        self.student_count += 1
        student.student_id = self.student_count
        self.students.append(student)

    def register_professor(self, professor : Professor):
        self.professor_count += 1
        professor.worker_code = self.professor_count
        self.professors.append(professor)

    def register_intern(self, intern : Intern):
        self.intern_count += 1
        intern.intern_id = self.intern_count
        self.interns.append(intern)

    def list_students(self):
        if self.students:
            for student in self.students:
                print(student.get_data())
            return
        print("no students")

    def list_professors(self):
        if self.professors:
            for professor in self.professors:
                print(professor.get_data())
            return
        print('no professors')

    def list_interns(self):
        if self.interns:
            for itern in self.interns:
                print(itern.get_data())
            return
        print('no interns')

    def list_all(self):
        print("-------- STUDENTS -----------")
        self.list_students()

        print("-------- PROFESSORS -----------")
        self.list_professors()

        print("-------- INTERNS -----------")
        self.list_interns()

class Person:

    def __init__(self, name, rg, cpf, adress, birthday):
        self.name = name
        self.rg = rg
        self.cpf = cpf
        self.adress = adress
        self.birthday = birthday

    def get_data(self):
        return f'Name: {self.name}\nRG: {self.rg}\nCPF: {self.cpf}\nAdress: {self.adress}\nRG: {self.birthday}'

class Professor(Person):

    def __init__(self, name, rg, cpf, adress, birthday, worker_code, disciplines, admission_date):
        super().__init__(name, rg, cpf, adress, birthday)
        self.worker_code = worker_code
        self.disciplines = disciplines
        self.admission_date = admission_date

    def get_professor_data(self):
        personal_data = super().get_data()
        disciplines_formatted = ", ".join(self.disciplines)

        return (
            f"{personal_data}\n"
            f"Worker Code: {self.worker_code}\n"
            f"Disciplines: {disciplines_formatted}\n"
            f"Admission Date: {self.admission_date}"
        )

class Student(Person):

    def __init__(self, name, rg, cpf, address, birthday,
                 student_id, enrollment_date, course, semester, fee_value):
        super().__init__(name, rg, cpf, address, birthday)
        self.student_id = student_id
        self.enrollment_date = enrollment_date
        self.course = course
        self.semester = semester
        self.fee = fee_value

    def calculate_fee(self):
        """Returns the monthly fee for the student."""
        return self.fee

    def get_data(self):
        personal_data = super().get_data()
        return (
            f"{personal_data}\n"
            f"Student ID: {self.student_id}\n"
            f"Enrollment Date: {self.enrollment_date}\n"
            f"Course: {self.course}\n"
            f"Semester: {self.semester}\n"
            f"Monthly Fee: ${self.calculate_fee():,.2f}"
        )
    
class Intern(Student):
    """aka a better version of a student, who's still a person"""

    def __init__(self, name, rg, cpf, address, birthday, student_id, enrollment_date, course, semester, fee_value, 
                 intern_enrollment_date, salary):
        super().__init__(name, rg, cpf, address, birthday, student_id, enrollment_date, course, semester, fee_value)
        self.intern_enrollment_date = intern_enrollment_date
        self.salary = salary
        self.fee = 0 # interns dont pay any fees

    def calculate_fee(self):
        """Interns do not pay fees."""
        return 0

    def get_data(self):
        student_data = super().get_data()
        return (
            f"{student_data}\n"
            f"Intern ID: {self.intern_id}\n"
            f"Intern Start Date: {self.intern_enrollment_date}\n"
            f"Salary: ${self.salary:,.2f}"
        )

def menu():
    school = School()

    while True:
        print("\n======== SCHOOL MANAGEMENT SYSTEM =========")
        print("1 - Register Student")
        print("2 - Register Professor")
        print("3 - Register Intern")
        print("4 - List Students")
        print("5 - List Professors")
        print("6 - List Interns")
        print("7 - List All")
        print("0 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\n--- Register Student ---")
            name = input("Name: ")
            rg = input("RG: ")
            cpf = input("CPF: ")
            address = input("Address: ")
            birthday = input("Birthday: ")
            enrollment_date = input("Enrollment Date: ")
            course = input("Course: ")
            semester = input("Semester: ")
            fee = float(input("Monthly Fee: "))

            student = Student(
                name, rg, cpf, address, birthday,
                enrollment_date, course, semester, fee
            )
            school.register_student(student)

        elif choice == "2":
            print("\n--- Register Professor ---")
            name = input("Name: ")
            rg = input("RG: ")
            cpf = input("CPF: ")
            address = input("Address: ")
            birthday = input("Birthday: ")
            disciplines = input("Disciplines (comma separated): ").split(",")
            admission_date = input("Admission Date: ")

            professor = Professor(
                name, rg, cpf, address, birthday,
                disciplines,
                admission_date
            )
            school.register_professor(professor)

        elif choice == "3":
            print("\n--- Register Intern ---")
            name = input("Name: ")
            rg = input("RG: ")
            cpf = input("CPF: ")
            address = input("Address: ")
            birthday = input("Birthday: ")
            enrollment_date = input("Student Enrollment Date: ")
            course = input("Course: ")
            semester = input("Semester: ")
            intern_start = input("Intern Start Date: ")
            salary = float(input("Salary: "))

            intern = Intern(
                name, rg, cpf, address, birthday,
                enrollment_date, course, semester, 0,
                intern_start, salary
            )
            school.register_intern(intern)

        elif choice == "4":
            print("\n--- Students ---")
            school.list_students()

        elif choice == "5":
            print("\n--- Professors ---")
            school.list_professors()

        elif choice == "6":
            print("\n--- Interns ---")
            school.list_interns()

        elif choice == "7":
            print("\n--- All People ---\n")
            school.list_all()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    menu()