#Physics Calculator

formula = float(input("What formula do you want? Density(1), Pressure(2), Work(3), Speed(4), Charge(5), Resistance(6), Power(7), Kinetic Energy(8), Gravitational Energy(9), Acceleration(10)"))
if formula == 1:

    Mass = float(input("Give me the Mass"))
    Volume = float(input("Give me the volume"))
    Density = Mass/Volume
    print(Density)

elif formula == 2:

    Force = float(input("Give me the Force"))
    Area = float(input("Give me the Area"))
    Pressure = Force/Area
    print(Pressure)

elif formula == 3:

    Force = float(input("Give me the Force"))
    Distance = float(input("Give me the Distance"))
    Work = Force*Distance
    print(Work)

elif formula == 4:

    Distance = float(input("Give me the Distance"))
    Time = float(input("Give me the Time"))
    Speed = Distance/Time
    print(Speed)
    
elif formula == 5:

    Current = float(input("Give me the Current"))
    Time = float(input("Give me the Time"))
    Charge = Current*Time
    print(Charge)
    

    

    
                   

                      
