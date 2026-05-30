class Customer:
    def __init__(self,id,name,location,contact):
        self.id=id
        self.name= name
        self.location=location
        self.contact=contact
        cus1 = {"id":id,"name":name,"location":location,"contact":contact}
        
class Agent:
    agent1= {"id":1,"name":"Ravi","location":"Chennai","contact":555,"availability":False}
    agent2={"id":2,"name":"ram","location":"Chennai","contact":999,"availability":False}
    agent3={"id":3,"name":"krish","location":"Madhavaram","contact":111,"availability":False}
def package_details():
    weight=float(input("Enter the weight of the package in kg:"))
    if weight>0:
        pickup_day=input("Enter the pickup day (Monday, Tuesday):")
        delivery_day=input("Enter the delivery day (Monday, Tuesday):")
        source=input("Enter source location:")
        destination=input("Enter destination location:")
        return weight,pickup_day,delivery_day,source,destination
    else:
        print("Weight must be greater than zero")

def assign_agent(customer_location):
    if customer_location == Agent.agent1["location"] and not Agent.agent1["availability"]:
        Agent.agent1["availability"]=True
        return Agent.agent1
    elif customer_location == Agent.agent2["location"] and not Agent.agent2["availability"]:
        Agent.agent2["availability"]=True
        return Agent.agent2
    elif customer_location == Agent.agent3["location"] and not Agent.agent3["availability"]:
        Agent.agent3["availability"]=True
        return Agent.agent3
    else:
        if not Agent.agent1["availability"]:
            Agent.agent1["availability"]=True
            return Agent.agent1
        elif not Agent.agent2["availability"]:
            Agent.agent2["availability"]=True
            return Agent.agent2
        elif not Agent.agent3["availability"]:
            Agent.agent3["availability"]=True
            return Agent.agent3
        else:
            print("All agents are currently unavailable. Please try again later.")
while True:
    print("1.Place order")
    print("2.Payment section")
    print("3.Track order")
    print("4.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        new_user= Customer(4,"Sam","Delhi",55658)
        print(new_user)
        weight,pickup_day,delivery_day,source,destination=package_details()
        print("Package details recorded successfully.")
        assigned_agent=assign_agent(destination)
        print("Assigned agent:",assigned_agent)
    elif choice ==2:
        print("Payment section")
    elif choice== 3:
        print("Tracking order")
    elif choice ==4:
        print("Exiting the system.thank you")
        break
    else:
        print("Invalid choice.Please try again")