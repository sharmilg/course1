#You are tasked with building a small library system using Python classes and
# inheritance. The system should track Person (name, age, gender), Member(inherits
# Person, membership), and Author(inherits Person, books_written) classes, along with
# a combined class, AuthorMember (inherits Member, Author), representing people who are
# both authors and members of the library. The library will manage memberships, books
# authored, and a brief introduction for each person.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        pass


class Member(Person):
    def __init__(self, name, age, gender, membership):
        super().__init__(name, age, gender)
        self.membership = membership

    def introduce(self):
        pass


class Author(Person):
    def __init__(self, name, age, gender, books_written):
        super().__init__(name, age, gender)
        self.books_written = books_written

    def introduce(self):
        pass

class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership, books_written):
        Member.__init__(self, name, age, gender, membership)
        Author.__init__(self, name, age, gender, books_written)

    def introduce(self):
        return f"{super(Member, self).introduce()} I have written {self.books_written} books."


# Example usage
person1 = Person("Sita", 30, "female")
person2 = Member("Hari", 40, "male", "basic")
person3 = Author("Ram", 50, "male", "ABC")
person4 = AuthorMember("Diya", 35, "female", "premium", "CDE")

print(person1.introduce())
print(person2.introduce())
print(person3.introduce())
print(person4.introduce())
