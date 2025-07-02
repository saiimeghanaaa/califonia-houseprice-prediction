# California-houseprice-prediction

Project Description: 
This project is a Machine Learning-based web application that predicts the median house price in California based on various input features such as average number of rooms, population, and location-related attributes. 
It uses the California Housing dataset from Scikit-learn, performs data preprocessing, exploratory data analysis (EDA), feature scaling, and trains a Linear Regression model to make predictions. The trained model is deployed using Streamlit Cloud, allowing users to interact with it via a simple and intuitive web interface. 

Key Features: 
• Predict house prices based on user inputs 
• Uses Linear Regression for prediction 
• Trained on the California Housing dataset 
• Clean, responsive UI using Streamlit 
• Fully deployed online via Streamlit Cloud 

Technologies Used for ML model: 
Python – Main language used to build the entire project. 
Easy to write, widely supported for ML and web apps. 
Pandas – Used for data loading and preprocessing. 
Helps handle tabular data like a spreadsheet. 
NumPy – Used for numerical operations and arrays. 
Makes computations fast and efficient. 
Scikit-learn – Used for model building and evaluation. 
Handled train-test split, scaling, regression, and metrics. 
Matplotlib – For basic data visualizations. 
Used to draw plots like histograms and line charts. 
Seaborn – For advanced, prettier visualizations. 
Helpful for heatmaps and spotting feature correlations. 
Pickle – To save and load the trained model. 
Avoids retraining every time we use the app. 
Streamlit – Used to create the web app interface. 
Makes the model interactive and user-friendly. 
Git & GitHub – For version control and code hosting. 
Helps deploy the project using Streamlit Cloud. 

Goal: 
To provide a quick and easy tool for real estate professionals, data enthusiasts, 
and students to explore how different factors affect housing prices in California. 

Deployment Workflow (Streamlit Cloud) 

Step 1: Prepare Project Folder 
project/ 
├── main.py              
├── regmodel.pkl         
← Streamlit UI script 
← Trained ML model (Pickle) 
├── requirements.txt     ← Required Python libraries 
└── README.md            
← (Optional) Project details 

Step 2: Create requirements.txt 
Include all dependencies used in your main.py: 
streamlit 
pandas 
numpy 
scikit-learn 

Step 3: Push to GitHub 
1. Create a new public GitHub repository (e.g., house-price-predictor) 
2. Push the following files: 
o main.py 
o regmodel.pkl 
o requirements.txt 
o README.md (optional)

Step 4: Deploy to Streamlit Cloud 
1. Go to https://streamlit.io/cloud 
2. Sign in with GitHub 
3. Click "New app" 
4. Select: 
o Your GitHub repository 
o main file: main.py 
o branch: main or master 
5. Click "Deploy" 
Streamlit will auto-install packages from requirements.txt and launch your app

Step 5: Done! 
• Your ML Web App is live! 
• You’ll get a public link to share or use
