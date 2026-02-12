class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"

print(Product("Mouse", 150))
# Product(name='Mouse', price=150)

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def __repr__(self):
        return f"Task(title={self.title!r}, done={self.done})"

t = Task("OOP o'rganish")
print("Yangi task:", t)
# Yangi task: Task(title="OOP o'rganish", done=False)
