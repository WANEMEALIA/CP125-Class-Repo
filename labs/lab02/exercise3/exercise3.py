# Lab 02 Exercise 3: Secure Vault System
# Write your code below:

def validate_entry(name, pin):
    if name == "Director" :
        if pin == 1122 :
            return True
        else: 
            return False
    elif name == "Security" :
        if pin == 9900 :
            return True
        else:
            return False
    else: 
        return False
# Test your code here
print("Testing Secure Vault System...")
