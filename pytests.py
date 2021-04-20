import pytest
from main import bmiMapper


#1 with correct URL
def test_normal_flow():
    assert bmiMapper([{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",  "HeightCm": 167, "WeightKg": 82}]) == [{'Gender': 'Male',
  'HeightCm': 171,
  'WeightKg': 96,
  'bmi': 32.8,
  'BMI category': 'Normal Weight',
  'Health Risk': 'Low Risk'},
 {'Gender': 'Male',
  'HeightCm': 161,
  'WeightKg': 85,
  'bmi': 32.8,
  'BMI category': 'Normal Weight',
  'Health Risk': 'Low Risk'},
 {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77, 'bmi': 23.8},
 {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62, 'bmi': 22.5},
 {'Gender': 'Female',
  'HeightCm': 150,
  'WeightKg': 70,
  'bmi': 31.1,
  'BMI category': 'Normal Weight',
  'Health Risk': 'Low Risk'},
 {'Gender': 'Female',
  'HeightCm': 167,
  'WeightKg': 82,
  'bmi': 29.4,
  'BMI category': 'Normal Weight',
  'Health Risk': 'Low Risk'},
 {'Overweight Count': 0}]
    
#2 with wrong i/p
def test_wrong_input():
    with pytest.raises (Exception):
        bmiMapper([])

