class Product:
    Id:str
    Type:str
    Price:int
    
    def __init__(self,*args) -> None:
        self.Id = args[0]
        self.Type = args[1]
        self.Price = int(args[2])


n = int(input('How many products are there? : '))

products = [Product(*input().split()) for i in range(n)]

def getProduct(products) -> Product:
    while True:
        Id = input('Id : ')
        try:
            return [product for product in products if product.Id == Id][0]
        except:
            print("This id doesn't exist.")

product = getProduct(products)

while True:
    q = int(input('Q : '))
    if q == 0:
        break
    elif q == 1:
        print(product.Type)
    elif q == 2:
        print(product.Price)
    elif q == 3:
        product = getProduct(products)
