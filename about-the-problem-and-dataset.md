# About CHD: 
Coronary heart disease (CHD) is usually caused by a build-up of fatty deposits (atheroma) on the walls of the arteries around the heart (coronary arteries).
The build-up of atheroma makes the arteries narrower, restricting the flow of blood to the heart muscle. This process is called atherosclerosis. 
Your **risk** of developing atherosclerosis is significantly increased if you:
- smoke 
- have high blood pressure (hypertension) 
- have a high blood cholesterol level
- don't take regular exercise
- have diabetes
- being obese or overweight 
- Other risk factors for developing atherosclerosis include: 

For more information on the disease, and it's risk factors visit: [Coronary heart disease, NHC](https://www.nhs.uk/conditions/coronary-heart-disease/causes/)


# About the Dataset:
## Features: 
- male: int [0 or 1] </br>
  Gender. </br>
  1 if male, 0 if female.
- age: int
  Age of patient
- education: int
- currentSmoker: int
- cigsPerDay: int
- BPMeds: int
- prevalentStroke: int
- prevalentHyp: int
- diabetes: int
- totChol: int
- sysBP: int
- diaBP: int
- BMI: float 
- heartRate: int
- glucose: int

## Target:
- TenYearCHD: int [0 or 1] </br>
  Whether or not the patient will develop a Coronary heart disease in 10 years time. </br>
  1 for Yes, 0 for No.






*Source: [Framingham Heart study dataset](https://www.kaggle.com/amanajmera1/framingham-heart-study-dataset)*: 
The dataset is publically available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has 10-year risk of future coronary heart disease (CHD).The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes. Variables Each attribute is a potential risk factor. There are both demographic, behavioral and medical risk factors.
