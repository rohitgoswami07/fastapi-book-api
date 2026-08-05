from fastapi import FastAPI, Depends, HTTPException, status
from db import get_db, engine
import models, schemas, services
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/books/", response_model= list[schemas.Book])
def get_all_books(db: Session = Depends(get_db)):
     return services.get_books(db)

@app.post("/books/", response_model= schemas.Book,status_code= status.HTTP_201_CREATED)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
     return services.create_book(db, book)

@app.get("/books/{id}", response_model= schemas.Book )
def get_book_by_id(id: int, db: Session = Depends(get_db)):
     db_book = services.get_book(db, id)
     if db_book:
          return db_book
     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                         detail= "Invalid id or Book not found")

@app.put("/books/{id}", response_model= schemas.Book )
def update_book(book: schemas.BookCreate, id: int, db: Session = Depends(get_db)):
     db_update =  services.update_book(db,book,id)
     if not db_update:
          raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                              detail= "Book not found")
     return db_update

@app.delete("/books/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_book(id:int , db : Session = Depends(get_db)):
     del_book = services.delete_book(db,id)
     if not del_book:
          raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                              detail= "Book nhi Found")
     return

@app.patch("/books/{id}", response_model= schemas.Book)
def patch_book(
     id: int,
     book: schemas.BookUpdate,
     db: Session = Depends(get_db)
     ):
     updated_book = services.update_book_entry(db,id,book)
     if not updated_book:
          raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                              detail= "Book Not Found")
     return updated_book
