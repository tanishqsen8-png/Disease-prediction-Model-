# Disease Prediction System

## Overview

This project is a Machine Learning-based system that predicts diseases based on symptoms entered by the user. It uses multiple algorithms (Decision Tree, Random Forest, and KNN) and compares their performance to select the best model.

This README provides complete step-by-step instructions to set up and run the project from scratch.

---

## Project Structure

```bash id="p7x1v4"
Disease-Prediction-System/
│
├── disease_prediction.py
├── disease_dataset.csv
└── README.md
```

---

## Prerequisites

Make sure the following are installed on your system:

* Python (version 3.7 or above)
* pip (Python package manager)

To check Python version:

```bash id="o2p7i0"
python --version
```

---

## Step 1: Get the Project

### Option A: Clone using Git

```bash id="7d3e2l"
git clone <your-repository-link>
cd Disease-Prediction-System
```

### Option B: Download ZIP

* Download the project ZIP file
* Extract it
* Open the extracted folder in terminal

---

## Step 2: Set Up Virtual Environment (Recommended)

Create a virtual environment:

```bash id="k3f9sn"
python -m venv venv
```

Activate it:

**Windows:**

```bash id="x6z2a1"
venv\Scripts\activate
```

**Mac/Linux:**

```bash id="9g8h2q"
source venv/bin/activate
```

---

## Step 3: Install Dependencies

Install required Python libraries:

```bash id="c5t1jw"
pip install pandas numpy matplotlib scikit-learn
```

---

## Step 4: Configure Dataset

Ensure the dataset file is present in the project folder:

```bash id="m1q4bz"
disease_dataset.csv
```

### Dataset Format Requirements:

* Each column represents a symptom
* Values must be:

  * `0` → No
  * `1` → Yes
* The last column must be named:

```id="h2r7kc"
disease
```

---

## Step 5: Run the Project

Execute the Python script:

```bash id="v8n3yf"
python disease_prediction.py
```

---

## Step 6: Using the Application

After running the program, you will see:

```id="z3m7pl"
==== Disease Prediction System ====
1. Predict Disease
2. Exit
```

### To Predict a Disease:

1. Enter `1`
2. Provide input for each symptom (0 or 1)
3. The system will display the predicted disease

### To Exit:

* Enter `2`

---

## Example

### Input:

```id="y1k8ds"
fever: 1
cough: 1
headache: 0
fatigue: 1
```

### Output:

```id="n9c4ux"
Predicted Disease: Flu
```

---

## How the System Works

1. Loads dataset using Pandas
2. Splits data into training and testing sets
3. Trains three models:

   * Decision Tree
   * Random Forest
   * KNN
4. Evaluates models using accuracy
5. Selects a model for prediction
6. Takes user input and predicts disease

---

## Troubleshooting

| Problem                | Solution                         |
| ---------------------- | -------------------------------- |
| Python not recognized  | Reinstall Python and add to PATH |
| Module not found error | Run `pip install <module>`       |
| Dataset not found      | Ensure file is in same folder    |
| Invalid input          | Enter only 0 or 1                |

---

## Notes

* This project is for educational purposes only
* It should not be used for real medical diagnosis

---

## Author

Tanishq Sen
25BAI10450

