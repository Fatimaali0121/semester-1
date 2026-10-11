# Week 1.2, Session 2: Task 6

temperature = int(input("Enter the machine temperature in degree celsius: "))
pressure = int(input("Enter machine pressure in PSI: "))
operational_status = int(input("Enter machine operational status, 1 for operating 0 for stopped: "))

if temperature > 80 :
    print("temperature is too high, it is recommended to shut down the machine")

elif 80 >= temperature >= 50 :
    print("temperature within safe limits")

else:
    print("temperature is low, no action is needed")



if pressure > 100 :
    print("high pressure is detected, maintenance is recommended")

elif 100 >= pressure >= 70 :
    print("pressure is stable")

else:
    print("pressure is low, system operating normally")



if operational_status == 1:
    if temperature > 80 or pressure > 100 :
         print("machine is running in unsafe conditions, it is recommended to shut it down")
    else:
        print("machine is running normally")
else:
  print("machine is off, no action is needed.")

  

