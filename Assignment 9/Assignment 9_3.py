class Book:
  
   def __init__(self,id,title,author,price,rating):
        self.id=id
        self.title=title
        self.author=author
        self.price=price 
        self.rating=rating

class Book_store:

  def __init__(self):
        self.books=[]
  
  def find_book_by_id(self, book_id):
        for book in self._books:
            if(book._id == book_id):
                 print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
            
        return None

  def find_book_by_author(self, author_name):
       
        
        for book in self._books:
            if(book._author == author_name):
               print(f"{book.id},{book.title},{book.auBoothor},{book.price},{book.rating}")
        return None

  def find_book_by_rating(self, less_rating, high_rating):
        
        
        for book in self._books:
            if(less_rating <= book._rating and high_rating >= book._rating):
                 print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
                
        return None


  def find_book_by_price(self, low_price, high_price):
      
        
       for book in self._books:
           if(low_price <= book._price and book._price <= high_price):
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
                
       return None
  
  def info(self):
        print( f''Book Id: {self._id}, \tBook Name: {self._title},\tAuthor: {self._author},\tPrice: {self._price},\tRating: {self._rating}\n'')

  
  def add_book(self,book):
       self.books.append(book)

book1 = Book(1, 'python','Tom', 150,4.3)
book2 = Book(2, 'SQL','Bob', 100, 2.5)
book3 = Book(3, 'Datascience','Mick',300,4.5)

s=Book_store()
s.add_book(book1)
s.add_book(book2)
s.add_book(book3)

s.info()

s.find_book_by_author("Bob")
s.find_book_by_rating(3,5)

s.find_book_by_price(50,200)

s. find_book_by_id(102)
    
                
                
       
    
 
