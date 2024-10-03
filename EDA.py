#only keeping course, nationality, age, gender and grade @ 1st semester
cols_to_keep = ["Course", "Nacionality", "Gender", "Age at enrollment",
                "Curricular units 1st sem (grade)", "Curricular units 2nd sem (grade)",
                "Curricular units 1st sem (enrolled)", "Curricular units 2nd sem (enrolled)"]

df_selected = df[cols_to_keep].copy()

print("Shape: ", df_selected.shape)
df_selected.head()

#take out people who dropped out
df_selected['Curricular_units_1st_sem_(grade)'] = df_selected['Curricular units 1st sem (grade)'].astype(str)
df_selected['Curricular_units_2nd_sem_(grade)'] = df_selected['Curricular units 2nd sem (grade)'].astype(str)

df_analysis = df_selected[
    (df_selected['Curricular_units_1st_sem_(grade)'] != "0.0") &
    (df_selected['Curricular_units_2nd_sem_(grade)'] != "0.0")
    ].copy()

df_analysis.rename(columns={
    'Curricular units 1st sem (grade)': 'Semester1Grade',
    'Curricular units 2nd sem (grade)': 'Semester2Grade',
    'Age at enrollment': 'Age'
    }, inplace=True)

#making sure that observations are taken out
num_variables = df.shape[1]
num_observations = df.shape[0]

num_variables_analysis = df_analysis.shape[1]
num_observations_analysis = df_analysis.shape[0]

print("df:")
print(f"Number of Variables: {num_variables}")
print(f"Number of Observations: {num_observations}")

print("\ndf_analysis:")
print(f"Number of Variables: {num_variables_analysis}")
print(f"Number of Observations: {num_observations_analysis}")

print(df_analysis.dtypes)