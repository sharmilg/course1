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
        Person.__init__(self,name, age, gender)
        self.membership = membership

    def introduce(self):
        pass


class Author(Person):
    def __init__(self, name, age, gender, books_written):
        Person.__init__(self,name, age, gender)
        self.books_written = books_written

    def introduce(self):
        pass

class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership, books_written):
        Member.__init__(self, name, age, gender, membership)
        Author.__init__(self, name, age, gender, books_written)

    def introduce(self):
        return f"I am {self.name}, {self.age} years old.I am {self.gender}. I have a {self.membership} membership and I have written book {self.books_written}"

members = []
member1 = AuthorMember("John",24,"Male","Platinum","CDE")
member2 = AuthorMember("Sita", 24,"Female", "basic","ABC")
members.append(member1)
members.append(member2)
for member in members:
    print(member.introduce())


