import datawarehouse as dw

usuario_1 = dw.UserAdmin(user_name= 'Alba',user_login= 'Gxwmm55')   
usuario_1.register()
# print(usuario_1.user_data(user_name= 'Alba',user_login= 'Gxwmm55'))
print(usuario_1.user_login)

usuario_2 = dw.UserUpdaters(user_name= 'Rocio',user_login= 'Sllxxxbb5')   
usuario_2.register()
print(usuario_2.user_data)

usuario_3 = dw.UserInvoicers(user_name= 'Estibaliz',user_login= 'Ysfma77dk')   
usuario_3.register()
print(usuario_3.user_data)



texto = dw.DictionaryFormatter(usuario_1.user_data)
print(texto.str_dictionary)


first_book = dw.Book(item_reference = 'A/B/2024-2000',
                  item_name = 'Fiesta',
                  item_pvp = 17.5,
                  item_description = "Libro de Ernest Hemingway"
                )
# print(first_book.item_main)
first_book.insert_book_details(book_name = 'Fiesta',
                               book_author = 'Ernest Hemingway',
                               book_pages = "150",
                               book_publisher = "Pan Books"
                               )




second_book = dw.Book(item_reference = 'A/B/2024-2001',
                  item_name = 'Romeo and Juliet',
                  item_pvp = 27.5,
                  item_description = "Libro de W. Shakespeare"
                )
# print(second_book.item_main)
second_book.insert_book_details(book_name = 'Romeo and Juliet',
                               book_author = 'William Shakespeare',
                               book_pages = "156",
                               book_publisher = "Letra Minúscula"
                              )

# print(first_book.item_main)
# print(second_book.item_main)


third_book = dw.Book(item_reference = 'A/B/2024-2002',
                  item_name = 'Damian',
                  item_pvp = 22,
                  item_description = "Libro de Herman Hess"
                )

third_book.insert_book_details(book_name = 'Damian',
                               book_author = 'Herman Hess',
                               book_pages = "136",
                               book_publisher = "Pan Books"
                              )

fourth_book = dw.Book(item_reference = 'A/B/2024-2003',
                   item_name = 'The Hobbit',
                   item_pvp = 29,
                   item_description = "Libro de J.R.R. Tolkien"
                  )

fourth_book.insert_book_details(book_name = 'The Hobbit',
                                book_author = 'J.R.R. Tolkien',
                                book_pages = "269",
                                book_publisher = "Letra Minúscula"
                               )
# print(second_book.book_description)

# print(str(first_book))
# print(repr(first_book))




libreria = dw.Library()
libreria.add_book(first_book.item_main)
libreria.add_book(second_book.item_main)
libreria.add_book(third_book.item_main)
libreria.add_book(fourth_book.item_main)

print('Contenido de libreria')
print(libreria.books_store)
# Si sobre escribo first_book
# libreria.books_store ={"nothing": "nothing to show"}

stock_libreria = libreria.list_of_books()
print(stock_libreria)






        
list_of_books = stock_libreria
print(list_of_books)
it = dw.Iterator(list_of_books)
process = iter(it)

print(next(process))
print(next(process))



