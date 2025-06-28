import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

DATASET_PATH = r"C:\Users\tiwar\OneDrive\Desktop\Python\leapGestRecog\00"
IMG_SIZE = 64


X = []
y = []

for gesture_name in os.listdir(DATASET_PATH):
    gesture_path = os.path.join(DATASET_PATH, gesture_name)
    if not os.path.isdir(gesture_path):
        continue
    for filename in os.listdir(gesture_path):
        img_path = os.path.join(gesture_path, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        X.append(img.flatten())
        y.append(gesture_name)

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
