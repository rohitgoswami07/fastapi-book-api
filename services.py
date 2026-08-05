from models import Book
from sqlalchemy.orm import Session
from schemas import BookCreate,BookUpdate

def create_book(db: Session, data: BookCreate):
     book_instance = Book(**data.model_dump())
     db.add(book_instance)
     db.commit()
     db.refresh(book_instance)
     return book_instance

def get_books(db: Session):
     return db.query(Book).all()

def get_book(db: Session, book_id: int):
     return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session,book: BookCreate, book_id: int):
     book_queryset =  db.query(Book).filter(Book.id == book_id).first()
     if book_queryset:
          for key,value in book.model_dump().items():
               setattr(book_queryset,key,value)
          db.commit()
          db.refresh(book_queryset)
     return book_queryset

def delete_book(db: Session, book_id: int):
     book_queryset =  db.query(Book).filter(Book.id == book_id).first()
     if book_queryset:
          db.delete(book_queryset)
          db.commit()
     return book_queryset

def update_book_entry(db: Session,book_id: int, book: BookUpdate):
     db_book = db.query(Book).filter(book_id == Book.id).first()
     if not db_book:
          return None
     update_data = book.model_dump(exclude_unset=True)

     for key,value in update_data.items():
          setattr(db_book,key,value)

     db.commit()
     db.refresh(db_book)
     return db_book
