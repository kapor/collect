# class BookRouter:
    
#     books_admin = "postgres"
#     default = "default"

#     def db_user(self, model, **hints):
#         BookList = model._meta.BookList
#         if BookList == 'book':
#             return self.books_admin
#         else:
#             return None

#     def db_for_write(self, model, **hints):
#         model_name = model._meta.model_name
#         if model_name == 'book':
#             return 'books'
#         else:
#             return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if model_name == 'book':
#             return db == 'books'
#         else:
#             return db == 'default'