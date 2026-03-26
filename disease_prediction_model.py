# ============================================
# Disease Prediction System (Final Version)
# ============================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# ============================================
# Load Dataset
# ============================================
def load_dataset(file_name):
    try:
        data = pd.read_csv(file_name)
        print("\nDataset loaded successfully!\n")
        return data
    except FileNotFoundError:
        print("Error: CSV file not found.")
        exit()


# ============================================
# Train Models
# ============================================
def train_models(X_train, y_train):
    models = {}

    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    models["Decision Tree"] = dt

    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    models["Random Forest"] = rf

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    models["KNN"] = knn

    return models


# ============================================
# Evaluate Models
# ============================================
def evaluate_models(models, X_test, y_test):
    accuracy_results = {}

    print("\nModel Performance:\n")

    for name, model in models.items():
        predictions = model.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        accuracy_results[name] = acc
        print(f"{name}: {round(acc * 100, 2)}%")

    return accuracy_results


# ============================================
# Select Best Model
# ============================================
def select_best_model(models, accuracy_results):
    best_model_name = max(accuracy_results, key=accuracy_results.get)
    print(f"\nBest Model Selected: {best_model_name}")
    return models[best_model_name]


# ============================================
# Prediction Function
# ============================================
def predict_disease(model, feature_names):
    print("\nEnter symptom values (0 = No, 1 = Yes):")

    user_input = []
    for feature in feature_names:
        value = int(input(f"{feature}: "))
        user_input.append(value)

    input_df = pd.DataFrame([user_input], columns=feature_names)

    prediction = model.predict(input_df)[0]

    # Optional: Confidence
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(input_df)
        confidence = max(prob[0]) * 100
        print(f"\nPredicted Disease: {prediction}")
        print(f"Confidence: {round(confidence, 2)}%")
    else:
        print(f"\nPredicted Disease: {prediction}")


# ============================================
# Main Program
# ============================================
def main():
    print("====== Disease Prediction System ======")

    data = load_dataset("disease_dataset.csv")

    X = data.drop("disease", axis=1)
    y = data["disease"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = train_models(X_train, y_train)

    accuracy_results = evaluate_models(models, X_test, y_test)

    best_model = select_best_model(models, accuracy_results)

    # Menu
    while True:
        print("\n1. Predict Disease")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            predict_disease(best_model, X.columns)
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


# Run program
if __name__ == "__main__":
    main()