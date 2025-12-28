import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Heart Disease EDA",
    layout="wide"
)

sns.set_theme(style="darkgrid", palette="deep")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("heart_disease_cleaned.csv")

df = load_data()

# ---------------- TITLE ----------------
st.title("❤️ Heart Disease Exploratory Data Analysis")
st.markdown("Clean dataset • BMI2 used • Full EDA replication")

# ---------------- BASIC INFO ----------------
st.subheader("Dataset Overview")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])
c3.metric("Min Age", int(df["Age"].min()))
c4.metric("Max Age", int(df["Age"].max()))

st.markdown("---")

# ---------------- AGE DISTRIBUTION ----------------
st.subheader("Age Distribution (30–79)")

fig, ax = plt.subplots(figsize=(12, 4))
sns.countplot(
    data=df,
    x="Age",
    color="#1f4ed8"
)
ax.set_title("Age Count (Every Age Shown)")
ax.tick_params(axis='x', rotation=90)
st.pyplot(fig)

# ---------------- HEART DISEASE vs AGE ----------------
st.subheader("Heart Disease vs Age")

fig, ax = plt.subplots(figsize=(12, 4))
sns.countplot(
    data=df,
    x="Age",
    hue="Heart_Disease"
)
ax.set_title("Heart Disease by Age")
ax.tick_params(axis='x', rotation=90)
st.pyplot(fig)

# ---------------- SMOKING vs HEART DISEASE ----------------
st.subheader("Smoking vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Smoking",
    hue="Heart_Disease"
)
ax.set_title("Smoking Status vs Heart Disease")
st.pyplot(fig)

# ---------------- GENDER vs HEART DISEASE ----------------
st.subheader("Gender vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Gender",
    hue="Heart_Disease"
)
ax.set_title("Gender vs Heart Disease")
st.pyplot(fig)


# ---------------- BMI2 CATEGORY vs HEART DISEASE ----------------
st.subheader("BMI2 Category vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="bmi2_category",
    hue="Heart_Disease"
)
ax.set_title("BMI2 Category vs Heart Disease")
st.pyplot(fig)


# ---------------- HYPERTENSION ----------------
st.subheader("Hypertension vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Hypertension",
    hue="Heart_Disease"
)
ax.set_title("Hypertension vs Heart Disease")
st.pyplot(fig)

# ---------------- DIABETES ----------------
st.subheader("Diabetes vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Diabetes",
    hue="Heart_Disease"
)
ax.set_title("Diabetes vs Heart Disease")
st.pyplot(fig)

# ---------------- HYPERLIPIDEMIA ----------------
st.subheader("Hyperlipidemia vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Hyperlipidemia",
    hue="Heart_Disease"
)
ax.set_title("Hyperlipidemia vs Heart Disease")
st.pyplot(fig)

# ---------------- FAMILY HISTORY ----------------
st.subheader("Family History vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Family_History",
    hue="Heart_Disease"
)
ax.set_title("Family History vs Heart Disease")
st.pyplot(fig)

# ---------------- PREVIOUS HEART ATTACK ----------------
st.subheader("Previous Heart Attack vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Previous_Heart_Attack",
    hue="Heart_Disease"
)
ax.set_title("Previous Heart Attack vs Heart Disease")
st.pyplot(fig)

# ---------------- ALCOHOL ----------------
st.subheader("Alcohol Intake vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Alcohol_Intake",
    hue="Heart_Disease"
)
ax.set_title("Alcohol Intake vs Heart Disease")
st.pyplot(fig)

# ---------------- PHYSICAL ACTIVITY ----------------
st.subheader("Physical Activity vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Physical_Activity",
    hue="Heart_Disease"
)
ax.set_title("Physical Activity vs Heart Disease")
st.pyplot(fig)

# ---------------- DIET ----------------
st.subheader("Diet vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Diet",
    hue="Heart_Disease"
)
ax.set_title("Diet vs Heart Disease")
st.pyplot(fig)

# ---------------- STRESS LEVEL ----------------
st.subheader("Stress Level vs Heart Disease")

fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(
    data=df,
    x="Stress_Level",
    hue="Heart_Disease"
)
ax.set_title("Stress Level vs Heart Disease")
st.pyplot(fig)

# ---------------- DATA PREVIEW ----------------
st.markdown("---")
st.subheader("Filtered Data Preview")
st.dataframe(df.head(50))
