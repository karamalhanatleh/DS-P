# Suppose you are purchasing something online on the Internet.
#  At the website, you get a 10% discount if you are a member. 
#  Additionally, you are also getting a discount of 5%onthe item
#  because its Father’s Day. Write a function that takes as input
#  the cost of the item that you are purchasing and a Boolean 
#  variable indicating whether you are a member (or not), applies
#  the discounts appropriately, and returns the final discounted value 
#  of the item.


def dis(cost_produt):
    print('const proudct is : ',cost_produt)
    member = (input("are you a member in website (y/n)"))

    dis_member = 0.10*cost_produt
    dis_fatherDay = 0.05*cost_produt
    the_final_discounted = dis_member+dis_fatherDay

    print(member)
    if member == "y":

        cost_produt -= dis_member

        cost_produt -= dis_fatherDay
        print("Const Produt after discount is :", cost_produt)
        return "the amount is the discount ", the_final_discounted

    elif member=="n":
            print("Sorry, there is no discount for you")
    else:
        print('sory , tyr again')
        
        
cost_produt=float(input("enter the cost proudct please: "))       


print(dis(cost_produt))