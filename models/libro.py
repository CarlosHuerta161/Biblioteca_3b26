class Libro:

    #constructor
    def __init__(self, id, titulo, autor, isbn, disponble):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponble

    def  prestar(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True

    def mostrar_info(self):
        disponible = "Disponible" if self.disponible else "no disponible" 
        return f"id: {self.id}, Titulo: {self.titulo}, Autor:{self.autor}, ISBN:{self.isbn}, Estado:{disponible}"
    
    