class Pizza:
    def __init__(self,size,toppiings,cheese):
        self.size=size
        self.toppings=toppiings
        self.cheese=cheese
    def price(self):
        self.cost=0
        if self.size=="small":
            self.cost+=50
        elif self.size=="medium":
            self.cost+=100
        else:
            self.cost+=200
        t20=["corn","tomato","onion","capsicum"]
        t50=["mushroom","olives","broccoli"]
        for t in self.toppings:
            if t in t20:
                self.cost+=20
            else:
                self.cost+=50
        self.cost+=50*len(self.cheese)
        return self.cost
class Order:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def order(self,n):
        self.pizzas=[]
        for i in range(n):
            t=[]
            c=[]
            print("customer pizza ",i+1)
            size=input("select size ")
            x=int(input("how many topping "))
            for i in range(x):
                try:
                    a=input("Enter topping ")
                    if a not in["corn","tomato","onion","capsicum","mushroom","olives","broccoli"]:
                        raise Except("Enter vaild topping")
                    t.append(a)
                except Exception as e:
                    print(e)
                x=int(input("how many cheese "))
                for i in range(x):
                    b=input("Enter cheese ")
                    c.append(b)
                self.pizzas.append(Pizza(size,t,c))
    def bill(self):
        self.total=0
        count=1
        for p in self.pizzas:
            print(p.size,p.toppings,p.cheese)
            self.total+=p.price()
            count+=1
        print("Total bill : ",self.total)
n=int(input("How many pizza to order : "))
o=Order("abc",1)
o.order(n)
o.bill()