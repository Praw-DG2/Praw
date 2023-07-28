import tkinter as tk
from tkinter import messagebox


class DigitalLibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Library")
        self.books = {}

        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.author_label = tk.Label(root, text="Author:")
        self.author_label.pack()
        self.author_entry = tk.Entry(root)
        self.author_entry.pack()

        self.year_label = tk.Label(root, text="Publication Year:")
        self.year_label.pack()
        self.year_entry = tk.Entry(root)
        self.year_entry.pack()

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack()

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()

        self.search_button = tk.Button(root, text="Search by Title", command=self.search_by_title)
        self.search_button.pack()

        self.results_text = tk.Text(root, height=10, width=50)
        self.results_text.pack()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        publication_year = int(self.year_entry.get())
        book_id = len(self.books) + 1
        self.books[book_id] = {
            'title': title,
            'author': author,
            'publication_year': publication_year
        }
        messagebox.showinfo("Book Added", f"Book with ID {book_id} added to the library.")

    def search_by_title(self):
        search_title = self.search_entry.get().lower()
        found_books = []
        for book_id, book_info in self.books.items():
            if search_title in book_info['title'].lower():
                found_books.append((book_id, book_info))

        self.display_search_results(found_books)

    def display_search_results(self, found_books):
        self.results_text.delete(1.0, tk.END)
        if found_books:
            self.results_text.insert(tk.END, "Found books:\n")
            for book_id, book_info in found_books:
                self.results_text.insert(tk.END, f"Book ID: {book_id}\n")
                self.results_text.insert(tk.END, f"Title: {book_info['title']}\n")
                self.results_text.insert(tk.END, f"Author: {book_info['author']}\n")
                self.results_text.insert(tk.END, f"Publication Year: {book_info['publication_year']}\n")
                self.results_text.insert(tk.END, '-' * 30 + '\n')
        else:
            self.results_text.insert(tk.END, "No books found.\n")


if __name__ == "__main__":
    root = tk.Tk()
    library_gui = DigitalLibraryGUI(root)
    root.mainloop()
