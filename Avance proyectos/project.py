import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from autogluon.tabular import TabularPredictor

# Función para convertir rangos a su valor medio
def convert_range_to_mean(value):
    if isinstance(value, str) and '-' in value:
        start, end = value.split('-')
        return (float(start) + float(end)) / 2
    return value

# Función principal
def run():
    st.set_page_config(page_title="Detección de EPOC", page_icon="🩺")
    st.write("# Detección de EPOC 🫁")
    st.markdown("""
        Sube un archivo .xlsx con los datos del paciente y los datos de espirometría 
        para analizar y determinar si el paciente tiene EPOC.
    """)

    uploaded_file = st.file_uploader("Cargar archivo .xlsx o .csv", type=["csv"])

    if uploaded_file is not None:
        try:
            # Cargar el archivo Excel
            df = pd.read_csv(uploaded_file, sep=';')
            
            # Verificar si faltan datos necesarios
            missing_data = False
            required_columns = ['Age', 'Gender', 'Height [cm]', 'Weight [kg]', 'History of Smoking (yes/no)', 
                                'Smoking Frequency', 'History of vaping (yes/no)', 'Frequency of vaping', 
                                'Asthma (yes/no and severity)']
            for col in required_columns:
                if col not in df.columns:
                    missing_data = True
                    break
                
            if missing_data:
                st.warning("Faltan datos en el archivo subido. Por favor, completa los datos del paciente a continuación:")
                peep = st.selectbox("PEEP", [0, 4, 8])
                age = st.number_input("Edad", min_value=0, max_value=120, step=1)
                gender = st.selectbox("Género", ["Male", "Female"])
                height_cm = st.number_input("Altura (cm)", min_value=0.0, step=0.1)
                weight_kg = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
                history_of_smoking = st.selectbox("Historial de Fumar (sí/no)", ["yes", "no"])
                smoking_frequency = st.selectbox("Frecuencia de Fumar", ["Never", "Occasionally", "Regularly"])
                history_of_vaping = st.selectbox("Historial de Vapear (sí/no)", ["yes", "no"])
                frequency_of_vaping = st.selectbox("Frecuencia de Vapear", ["Never", "Occasionally", "Regularly"])
                asthma = st.selectbox("Asma (sí/no y severidad)", ["no", "mild", "moderate", "severe"])

                datos_paciente = {
                    "Subject Number" : [1],
                    "PEEP": [peep],
                    "Age": [age],
                    "Gender": [gender],
                    "Height [cm]": [height_cm],
                    "Weight [kg]": [weight_kg],
                    "History of Smoking (yes/no)": [history_of_smoking],
                    "Smoking Frequency": [smoking_frequency],
                    "History of vaping (yes/no)": [history_of_vaping],
                    "Frequency of vaping": [frequency_of_vaping],
                    "Asthma (yes/no and severity)": [asthma]
                }
                df = pd.concat([df, pd.DataFrame(datos_paciente)], ignore_index=True)
                test_patient_ids = [1]    
            
            else:

                # Rellenar los espacios en blanco en las columnas especificadas
                df['Smoking Frequency'] = df['Smoking Frequency'].fillna('Never')
                df['Frequency of vaping'] = df['Frequency of vaping'].fillna('Never')

                # Aplicar la función a las columnas numéricas
                num_cols = ['Height [cm]']
                df[num_cols] = df[num_cols].applymap(convert_range_to_mean)
                
                # Dividir el conjunto de datos en función del paciente
                patient_ids = df['Subject Number'].unique()
                test_patient_ids = st.selectbox("Selecciona el ID del paciente", patient_ids)
                selected_peep_level = st.selectbox("Selecciona el nivel de PEEP", [0, 4, 8])
                test_patient_ids = [test_patient_ids]
                
                #test_patient_ids = [7]  # Escoger al paciente nro 7
            
            
            
            if st.button("Analizar"):

                # Separar datos de prueba y entrenamiento
                test_df = df[df['Subject Number'].isin(test_patient_ids)].copy()
                train_df = df[~df['Subject Number'].isin(test_patient_ids)]

                # Crear conjuntos de características y etiquetas
                #X_train = train_df.drop(columns=['Subject Number', 'COPD'])
                #y_train = train_df['COPD']
                X_test = test_df.drop(columns=['Subject Number'])
                #X_test = test_df.drop(columns=['Subject Number', 'COPD'])
                #y_test = test_df['COPD']

                # Definir las columnas categóricas y numéricas
                categorical_features = ['Gender', 'History of Smoking (yes/no)', 'Smoking Frequency', 'History of vaping (yes/no)', 'Frequency of vaping','Asthma (yes/no and severity)']
                numerical_features = ['Age', 'Height [cm]', 'Weight [kg]', 'PEEP', 'Time [s]', 'Pressure [cmH2O]', 'Flow [L/s]', 'V_tidal [L]']

                # Crear el transformador de columnas
                preprocessor = ColumnTransformer(
                    transformers=[
                        ('num', StandardScaler(), numerical_features),
                        ('cat', OneHotEncoder(), categorical_features)
                    ])

                # Preprocesar las características
                #X_train = preprocessor.fit_transform(X_train)
                X_test = preprocessor.fit_transform(X_test)

                # Crear un DataFrame combinado para AutoGluon
                #train_data = pd.DataFrame(X_train, columns=preprocessor.get_feature_names_out())
                #train_data['COPD'] = y_train.values
                test_data = pd.DataFrame(X_test, columns=preprocessor.get_feature_names_out())
                #test_data['COPD'] = y_test.values

                # Cargar el predictor de AutoGluon
                predictor = TabularPredictor.load(r'C:\Users\ldani\Documents\Patronus\Project\AutogluonModels\best')

                # Hacer predicciones en el conjunto de prueba
                #predictions = predictor.predict(test_data.drop(columns=['COPD']))
                predictions = predictor.predict(test_data)
                #predictions_subset = predictions[16800:20160]
                #st.write("Predicciones de COPD:")
                #st.write(predictions_subset)
                
                # Agregar las predicciones al dataframe de prueba para verlas en contexto
                test_data['Predicted_COPD'] = predictions
                
                # Filtrar las filas de acuerdo al nivel de PEEP seleccionado
                if selected_peep_level == 0:
                    media = test_data[['Predicted_COPD']].iloc[0:13440].mean()
                elif selected_peep_level == 4:
                    media = test_data[['Predicted_COPD']].iloc[13441:26880].mean()
                else:  # selected_peep_level == 8
                    media = test_data[['Predicted_COPD']].iloc[26881:40319].mean()

                
                #media = test_data[['Predicted_COPD']].iloc[:].mean()
                #media = test_data[['Predicted_COPD']].iloc[16800:20160].mean()
                st.write("El paciente tiene nivel de EPOC:")
                st.write(media)

        except Exception as e:
            st.error(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    run()
