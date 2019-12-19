evaluate_risk(male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose):-

    age<= 46.5, sysBP <= 152.75, BMI <= 39.815, totChol <= 437.0.
    diaBP<= 95.0, BMI <= 39.815, sysBP <= 152.75, age <= 46.5.
    age<= 46.5, sysBP <= 152.75, heartRate <= 74.0, totChol<= 210.0.
    age<= 46.5, sysBP <= 152.75, heartRate <= 74.0, totChol<= 210.0, diaBP<=110.5.
    age<= 46.5, sysBP <= 152.75, heartRate <= 74.0, totChol<= 262.0, male <= 0.5.


    age<= 46.5, sysBP <= 144.25, heartRate <= 59.5, male <= 0.5, glucose <= 147.5.




    age > 46.5 , sysBP <= 144.25, glucose <= 147.5, BMI <= 36.415, diaBP <= 84.0.
    heartRate <= 59.5, male <= 0.5, glucose <= 147.5, sysBP <= 144.25.
    glucose <= 121.0, age <= 54.5, age > 46.5, male <=0.5, sysBP <= 144.25.
    sysBP <= 192.5, age <= 54.5, age > 46.5, male <= 0.5, sysBP <= 144.25.
    diaBP <= 86.75, glucose <= 92.5, male <= 0.5, sysBP <= 144.25, age > 46.5.





















