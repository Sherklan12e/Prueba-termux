from faker import Faker
from faker.providers import internet
fake = Faker()
fake.name()
fake.address()
fake.text()
fake = Faker()
fake.add_provider(internet)
def fakess():
    textos = ( "\nInformation: " + fake.text() +" \n ")
    direccion = ( "\nSu direccion es: " + fake.address()+ " \n ")
    ip = ( "\nSu ip es: " + fake.ipv4_private()+" \n ")
    nombres = ("\nSu nombre es: " + fake.name()+" \n ")
    informacion = nombres + ip + direccion + textos
    petecion = input("Quieres Informacion Fake si o no? :V ")
    if petecion =='si':
        print(informacion)
        
    elif petecion =='no':
        print("bueno chau xd 😠😠🥺😡")
    else:
        print("Que quisiste decir 🤨🤔🤔🤑😵 intenta denuevo")
fakess()

    
    
    
    

