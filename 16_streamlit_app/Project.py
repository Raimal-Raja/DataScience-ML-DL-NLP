import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Set page title and favicon
st.set_page_config(
    page_title="Iris Species Predictor",
    page_icon="🌸",
    layout="centered"
)

# Load data using Streamlit's caching decorator for efficiency
@st.cache_data
def load_data():
    """
    Loads the Iris dataset and returns a DataFrame and target names.
    The data is cached to avoid reloading on every rerun.
    """
    iris = load_iris()
    # Create a DataFrame from the Iris data, using feature names as columns
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    # Add the species (target) column to the DataFrame
    df['species'] = iris.target
    return df, iris.target_names

# Load the dataset and target names
df, target_names = load_data()

# Initialize and train the RandomForestClassifier model
# The features are all columns except the last one ('species')
# The target is the 'species' column
model = RandomForestClassifier(random_state=42) # Added random_state for reproducibility
model.fit(df.iloc[:, :-1], df['species'])

# --- Streamlit UI Elements ---

# Main title for the application
st.title('Iris Species Prediction App')
st.markdown("""
    This app predicts the **Iris species** based on input features
    using a Random Forest Classifier.
""")

# Section title for input features
st.header('Input Features')

# Create sliders for each feature, using min/max values from the dataset
# Corrected typos in column names: 'lenght' -> 'length'
sepal_length = st.slider(
    "Sepal Length (cm)",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max()),
    float(df['sepal length (cm)'].mean()) # Default to mean for initial value
)
sepal_width = st.slider(
    "Sepal Width (cm)",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max()),
    float(df['sepal width (cm)'].mean())
)
petal_length = st.slider(
    "Petal Length (cm)",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max()),
    float(df['petal length (cm)'].mean())
)
petal_width = st.slider(
    "Petal Width (cm)",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max()),
    float(df['petal width (cm)'].mean())
)

# Prepare the input data for prediction as a list of lists
# The model expects a 2D array-like input
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# --- Prediction Section ---
st.header('Prediction')

# Perform the prediction using the trained model
prediction = model.predict(input_data)
# Get the predicted species name using the target_names array
predicted_species = target_names[prediction[0]]

# Display the prediction result
st.success(f'The predicted Iris species is: **{predicted_species}**')

st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit and Scikit-learn.")
