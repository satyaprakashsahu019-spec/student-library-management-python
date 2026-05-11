"""
Date: 11 may 2026
Author: Satyaprakash Sahu
Project: Student library management system
"""
from datetime import date, timedelta


class Library:
    def __init__(self, listofBooks, categories=None):
        self.books = listofBooks
        self.categories = categories if categories is not None else {}

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" *-- " + book)
        print("\n")

    def displayCategories(self):
        if not self.categories:
            print("NO CATEGORIES AVAILABLE.\n")
            return

        print("\nAVAILABLE CATEGORIES:")
        category_names = list(self.categories.keys())
        for idx, category in enumerate(category_names, start=1):
            print(f"{idx}. {category}")
        print("\n")

    def getBooksByCategory(self, category_name):
        if category_name not in self.categories:
            return []
        category_books = self.categories[category_name]
        return [book for book in category_books if book in self.books]

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
        else:
            borrow_date = date.today()
            due_date = borrow_date + timedelta(days=7)
            track.append(
                {
                    "name": name,
                    "book": bookname,
                    "borrow_date": borrow_date,
                    "due_date": due_date,
                }
            )
            print(f"BOOK ISSUED TO {name}: THANK YOU, KEEP IT WITH CARE AND RETURN ON TIME.")
            print(f"BORROW DATE: {borrow_date}")
            print(f"RETURN BY (DUE DATE): {due_date}\n")
            self.books.remove(bookname)

    def returnBook(self, name, bookname):
        issued_record = None
        for record in track:
            if record["name"] == name and record["book"] == bookname:
                issued_record = record
                break

        if issued_record is None:
            print("NO SUCH ISSUED RECORD FOUND FOR THIS NAME AND BOOK.\n")
            return

        fine = 0
        today = date.today()
        if today > issued_record["due_date"]:
            late_days = (today - issued_record["due_date"]).days
            fine = late_days * 20

        track.remove(issued_record)
        print("BOOK RETURNED : THANK YOU! \n")
        if fine > 0:
            print(f"LATE RETURN FINE: Rs.{fine} (Rs.20/day)\n")
        else:
            print("NO FINE. RETURNED ON TIME.\n")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)

    def searchBook(self, keyword):
        keyword = keyword.lower().strip()
        matched_books = [book for book in self.books if keyword in book.lower()]

        if matched_books:
            print(f"\n{len(matched_books)} MATCHED BOOK(S):")
            for book in matched_books:
                print(" *-- " + book)
            print("\n")
        else:
            print("\nNO MATCHING BOOK FOUND.\n")


class Student():
    def requestBook(self, available_books):
        print("So, you want to borrow book!")
        if len(available_books) == 0:
            print("NO BOOKS AVAILABLE TO BORROW.\n")
            return None

        print("\nSELECT A BOOK BY NUMBER:")
        for idx, book in enumerate(available_books, start=1):
            print(f"{idx}. {book}")

        choice = int(input("Enter book number: "))
        if choice < 1 or choice > len(available_books):
            print("INVALID BOOK NUMBER.\n")
            return None
        return available_books[choice - 1]

    def returnBook(self):
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        return name, self.book

    def selectReturnBookFromHistory(self, issued_records):
        if len(issued_records) == 0:
            print("NO ISSUED BOOKS AVAILABLE TO RETURN.\n")
            return None

        print("\nYOUR ISSUED BOOK HISTORY:")
        for idx, record in enumerate(issued_records, start=1):
            print(
                f"{idx}. {record['book']} (Borrowed: {record['borrow_date']}, Due: {record['due_date']})"
            )

        choice = int(input("Enter book number to return: "))
        if choice < 1 or choice > len(issued_records):
            print("INVALID BOOK NUMBER.\n")
            return None
        return issued_records[choice - 1]["book"]

    def donateBook(self):
        print("Okay! you want to doante book!")
        self.book = input("Enter name of the book you want to donate: ")
        return self.book

    def chooseCategory(self, categories):
        if len(categories) == 0:
            print("NO CATEGORIES AVAILABLE.\n")
            return None

        print("\nSELECT A CATEGORY BY NUMBER:")
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category}")

        choice = int(input("Enter category number: "))
        if choice < 1 or choice > len(categories):
            print("INVALID CATEGORY NUMBER.\n")
            return None
        return categories[choice - 1]

    def searchAndSelectBook(self, available_books):
        keyword = input("Enter book name or keyword: ").strip().lower()
        matched_books = [book for book in available_books if keyword in book.lower()]

        if len(matched_books) == 0:
            print("NO MATCHING BOOK FOUND TO BORROW.\n")
            return None

        print("\nMATCHED BOOKS:")
        for idx, book in enumerate(matched_books, start=1):
            print(f"{idx}. {book}")

        choice = int(input("Enter book number to borrow: "))
        if choice < 1 or choice > len(matched_books):
            print("INVALID BOOK NUMBER.\n")
            return None
        return matched_books[choice - 1]


if __name__ == "__main__":
    categories = {
        "Programming": [
            "Clean Code",
            "The Pragmatic Programmer",
            "Introduction to Algorithms",
            "Python Crash Course",
            "You Don't Know JS",
            "Design Patterns",
        ],
        "Networking": [
            "Computer Networks Tanenbaum",
            "Computer Networking Kurose and Ross",
            "TCP/IP Illustrated",
            "Network Warrior",
            "DNS and BIND",
        ],
        "Cybersecurity": [
            "The Web Application Hackers Handbook",
            "Hacking The Art of Exploitation",
            "The Art of Invisibility",
            "Metasploit The Penetration Testers Guide",
            "Social Engineering The Science of Human Hacking",
        ],
        "Finance and Business": [
            "Rich Dad Poor Dad",
            "The Intelligent Investor",
            "Zero to One",
            "Think and Grow Rich",
            "The Lean Startup",
        ],
        "Self Help and Psychology": [
            "Psycho Cybernetics",
            "Atomic Habits",
            "The Power of Now",
            "Deep Work",
            "12 Rules for Life",
        ],
        "Strategy and Philosophy": [
            "The Art of War",
            "The Prince Machiavelli",
            "Meditations Marcus Aurelius",
            "48 Laws of Power",
            "The Book of Five Rings",
        ],
        "AI and Data Science": [
            "Artificial Intelligence Russell and Norvig",
            "Hands on Machine Learning",
            "Deep Learning Ian Goodfellow",
            "Data Science from Scratch",
            "The Hundred Page Machine Learning Book",
        ],
    }

    all_books = []
    for books in categories.values():
        all_books.extend(books)

    VSSUTlibrary = Library(all_books, categories)
    student = Student()
    track = []

    print("\t\t\t\t\t\t\t******* WELCOME TO THE VSSUT LIBRARY *******\n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. List all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. Browse by category\n7. Search books\n8. Exit\n""")

    while (True):
        # print(track)
        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing
                VSSUTlibrary.displayAvailableBooks()
            elif usr_response == 2:  # borrow
                borrower = input("Enter your name: ")

                print("\nCHOOSE BORROW METHOD:")
                print("1. Browse by category")
                print("2. Search and borrow directly by name")
                borrow_method = int(input("Enter your option: "))

                selected_book = None
                if borrow_method == 1:
                    category_names = list(VSSUTlibrary.categories.keys())
                    selected_category = student.chooseCategory(category_names)
                    if selected_category is not None:
                        category_books = VSSUTlibrary.getBooksByCategory(selected_category)
                        print(f"\nAVAILABLE BOOKS IN {selected_category}:")
                        if len(category_books) == 0:
                            print("NO BOOKS AVAILABLE IN THIS CATEGORY.\n")
                        else:
                            selected_book = student.requestBook(category_books)
                elif borrow_method == 2:
                    selected_book = student.searchAndSelectBook(VSSUTlibrary.books)
                else:
                    print("INVALID BORROW OPTION.\n")

                if selected_book is not None:
                    VSSUTlibrary.borrowBook(borrower, selected_book)
            elif usr_response == 3:  # return
                print("So, you want to return book!")
                borrower = input("Enter your name: ")
                user_issued_records = [
                    record for record in track if record["name"] == borrower
                ]

                if len(user_issued_records) == 0:
                    print("YOU HAVE NO ISSUED BOOKS TO RETURN.\n")
                else:
                    returning_book = student.selectReturnBookFromHistory(
                        user_issued_records
                    )
                    if returning_book is not None:
                        VSSUTlibrary.returnBook(borrower, returning_book)
            elif usr_response == 4:  # donate
                VSSUTlibrary.donateBook(student.donateBook())
            elif usr_response == 5:  # track
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
                else:
                    for issued in track:
                        print(
                            f"{issued['book']} is issued by {issued['name']} (Due: {issued['due_date']})"
                        )
                    print("\n")
            elif usr_response == 6:  # browse by category
                category_names = list(VSSUTlibrary.categories.keys())
                selected_category = student.chooseCategory(category_names)
                if selected_category is not None:
                    category_books = VSSUTlibrary.getBooksByCategory(selected_category)
                    print(f"\nAVAILABLE BOOKS IN {selected_category}:")
                    if len(category_books) == 0:
                        print("NO BOOKS AVAILABLE IN THIS CATEGORY.\n")
                    else:
                        for idx, book in enumerate(category_books, start=1):
                            print(f"{idx}. {book}")
                        print("\n")
            elif usr_response == 7:  # search
                keyword = input("Enter keyword to search: ")
                VSSUTlibrary.searchBook(keyword)
            
            elif usr_response == 8:  # exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:              #catch errors
            print(f"{e}---> INVALID INPUT! \n")