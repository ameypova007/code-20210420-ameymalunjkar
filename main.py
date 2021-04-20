import argparse
import ast
def bmiMapper(jsons):
    counts = 0
    for i in jsons:
        if "WeightKg" in i and "HeightCm" in i:
            i["bmi"] = round(i["WeightKg"]/((i["HeightCm"]/100)**2),1)
        else:
            i["bmi"] = 0
        if i["bmi"] < 18.4:
            i["BMI category"] = "Under weight"
            i["Health Risk"] = "Malnutrition Risk"
        elif 18.5 < i["bmi"] > 24.9:
            i["BMI category"] = "Normal Weight"
            i["Health Risk"] = "Low Risk"
        elif 25 < i["bmi"] > 29.9:
            i["BMI category"] = "Overweight"
            i["Health Risk"] = "Enhanced Risk"
            counts=+1
        elif 30 < i["bmi"] > 34.9:
            i["BMI category"] = "Moderately obese"
            i["Health Risk"] = "Medium Risk"
        elif 35  < i["bmi"] > 39.9:
            i["BMI category"] = "Severely obese"
            i["Health Risk"] = "High Risk"
        elif i["bmi"] > 40:
            i["BMI category"] = "Very severely obese "
            i["Health Risk"] = "Very High Risk"
    jsons.append({"Overweight Count" : counts})
    return jsons

if __name__ == '__main__':
    print(bmiMapper([{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",  "HeightCm": 167, "WeightKg": 82}]))