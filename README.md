# SCT_ML_4
This is a Hand Gesture Recognition model that can accurately identify and classify different hand gestures from image or video data enabling intuitive human computer interaction and gesture based control system| Internship @ SkillCraft Technologies

# ✋🤚 Hand Gesture Recognition using SVM

This project implements a machine learning model to classify **hand gestures** from images using a Support Vector Machine (SVM). It demonstrates fundamental techniques in image preprocessing and multi-class classification for computer vision tasks.

---

## 📌 Objective

🔎 Build a machine learning model to classify grayscale images into different **hand gesture classes** using a Support Vector Machine (SVM), aiming to:

- Understand multi-class image classification
- Practice image preprocessing and feature engineering
- Evaluate model performance on real-world gesture images

---

## 🗂️ Dataset Details

- **Dataset Name:** LeapGestRecog
- **Source:** [LeapGestRecog Dataset on Kaggle](https://www.kaggle.com/datasets/gti-upm/leapgestrecog)

### Folder Structure

| Folder / File Path                               | Description                                 |
|--------------------------------------------------|---------------------------------------------|
| leapGestRecog/                                   | Root folder for the dataset                 |
| leapGestRecog/00/                                | Folder for subject 00’s gesture images      |
| leapGestRecog/00/01_palm/                        | Folder containing palm gesture images       |
| leapGestRecog/00/01_palm/0_palm_neo_1_1.png      | Example image of palm gesture               |
| leapGestRecog/00/02_l_fist_moved/                | Folder containing left fist moved images    |
| leapGestRecog/00/02_l_fist_moved/0_l_fist_neo_1_1.png | Example image of left fist moved gesture |
| ...                                              | Other gesture folders for the subject       |

- Dataset contains images from multiple subjects performing various hand gestures.
- Each gesture type is stored in a separate subfolder.
- Images are grayscale and vary in size, so they are resized during preprocessing.

---

## 🧠 Techniques Used

- Grayscale image loading
- Image resizing to **64 × 64 pixels**
- Flattening images into 1D feature vectors
- Multi-class labels derived from folder names
- Support Vector Machine (SVM) with a linear kernel
- Train-test split (80% train, 20% test)
- Model evaluation using accuracy and classification report

---

## ✅ Output Example

### 📊 Model Evaluation Metrics:

Accuracy: 1.0

Classification Report:
                precision    recall  f1-score   support

      01_palm       1.00      1.00      1.00        36
         02_l       1.00      1.00      1.00        47
      03_fist       1.00      1.00      1.00        46
04_fist_moved       1.00      1.00      1.00        36
         02_l       1.00      1.00      1.00        47
      03_fist       1.00      1.00      1.00        46
04_fist_moved       1.00      1.00      1.00        36
     05_thumb       1.00      1.00      1.00        34
     06_index       1.00      1.00      1.00        34
        07_ok       1.00      1.00      1.00        33
08_palm_moved       1.00      1.00      1.00        44
         09_c       1.00      1.00      1.00        48
         02_l       1.00      1.00      1.00        47
      03_fist       1.00      1.00      1.00        46
04_fist_moved       1.00      1.00      1.00        36
04_fist_moved       1.00      1.00      1.00        36
     05_thumb       1.00      1.00      1.00        34
     06_index       1.00      1.00      1.00        34
     05_thumb       1.00      1.00      1.00        34
     05_thumb       1.00      1.00      1.00        34
     06_index       1.00      1.00      1.00        34
        07_ok       1.00      1.00      1.00        33
08_palm_moved       1.00      1.00      1.00        44
         09_c       1.00      1.00      1.00        48
      10_down       1.00      1.00      1.00        42

     accuracy                           1.00       400
    macro avg       1.00      1.00      1.00       400
 weighted avg       1.00      1.00      1.00       400

 ---

## 🚀 How to Run the Project

You can run this project locally using Python.

### 🔹 Option 1: Run Locally in VS Code

1. Download and extract the LeapGestRecog dataset from Kaggle.

2. Open the project folder in **Visual Studio Code**.

3. Ensure the correct Python interpreter is selected.

4. Update the dataset path in your Python script:

```python
DATASET_PATH = r"C:\Users\tiwar\OneDrive\Desktop\Python\leapGestRecog\00"

 
