# Predicting-Academic-Success-vs.-Dropout-Rate

CS105 Final Project (Team 7) Group Members - Ashwin Ramaseshan, Brian Uong, Lennon Chakkalakal, Aryan Bohra, Gursimar Jawanda

Project Proposal - Given variables such as nationality, marital status, gender, .etc, we will predict their academic success and dropout rate.

Dataset: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

This dataset was created to have several amount information from a college about students in various courses like farming, design, teaching, nursing, reporting, business, social work, and tech. This info includes what we know about students when they join college (their school background, where they come from, and their money situation) and how well they did in their first and second semesters. We're using this data to make a system that can guess if a student will drop out, do really well, or be somewhere in between, but there are a lot more students in one of these groups than the others.

We've selected the "Predict students' dropout and academic success" dataset from the UCI Machine Learning Repository. This dataset is sourced from a higher education institution, and comprises various undergraduate degrees including agronomy, design, education, nursing, journalism, management, social service, and technologies. Its primary objective is to determine the likelihood of a student dropping out or achieving academic success. The dataset uses a model that considers various factors such as academic trajectory, demographics, socio-economic background, and performance during the initial semesters. It has over 36 distinct features including a student's age, marital status, age at enrollment, units taken, and parental occupations, among many more. These features collectively provide insights into whether a student is more likely to drop out and underperform in their academics or succeed and excel. With this model, it can potentially assist educational institutions and academic advisors in identifying students who may require extra help to help them stay on course and succeed in their academics.

Slides Link: https://docs.google.com/presentation/d/1lbmzTPA8P0WTs4SfOS6c3h-3xuS4kgsvDz452LrFzyc/edit#slide=id.g2c3b3baea9c_3_4

Contribution:

Ashwin Ramaseshan- I contributed with the random forest and linear regression models. I also helped with analyzing these models along with analyzing the K means clustering.

Gursimar Jawanda : Made analysis on the different EDA graphs. Made questions needed to assess classmates.

Aaryan Bohra : Listed and explained the techniques used for predicting academic sucess and dropout rate.

Brian Uong-For my part I worked on data collection, data cleaning, eda, as well as worked on the presentation along with the rest of my group

Lennon Chakkalakal: Made the slides, formatted the report and helped on the random forest algothrim.

Techniques and Algothrims: Random Forest: The Random Forest classifier uses multiple decision trees and uses random samples of the data for each tree. This would help prevent the trees from becoming overly similar and overfitting the data. This means that it will be more accurate and precise at classifying our data. Random Forest classifier is a supervised learning training model in which the training data includes labeled examples. These labels provide the algorithm with the desired output for each data point. The algorithm learns the relationship between the input features and the labels, and uses this knowledge to predict labels for new, unseen data.

K-Means Clustering: K-means sorts data points into groups (clusters) based on how similar they are to each other. This similarity is typically determined by distance metrics. We used the elbow method in order to determine how many k-clusters we need the data to be divided into. This training model is unsupervised which means that it doesn't require labeled data. You provide the data points, and the algorithm finds the clusters.

Linear Regression: Linear regression assumes a linear relationship between variables. In this case, the relationship between factors like application mode or marital status and student outcomes (dropout/graduation) might not be perfectly linear. However, if the dataset was modified slightly, we could explore linear regression. For example we create a new target variable: Instead of dropout/enrolled/graduate, imagine a new variable is created that represents the number of credits a student completes in their first year. Independent Variables: We could include factors that might influence credits completed, such as: Hours studied per week, High school GPA, and Application order. With this modification, we could use linear regression to model the relationship between these factors and the number of credits completed in the first year. The model would estimate a linear equation to predict the expected number of credits a new student might complete based on their application order, GPA, and study habits.

Gradient Boosting: Gradient Boosting uses the prediction from multiple weaker models to create a single, but stronger prediction model. For the weaker models, we used decision trees for simple models based on a series of yes or no questions, or categorical questions. Since it uses weaker models as its training data, it is a supervised training technique.

K-Nearest Neighbors Classification: K-nearest neighbors categorizes new data points based on their similarity to existing labeled data points. The algorithm identifies the k nearest neighbors in the training set to the new data point. The new data point is then assigned the most frequent class label among these k nearest neighbors. So basically, the new point is categorized based on the "majority vote" of its closest neighbors. Since it relies on training data that has labels or variables, it is also a supervised learning training model.

Decision Trees: The decision tree is trained on a dataset with labeled examples. These labels represent the desired outcome you want to predict. They mimic human decision-making by learning a series of yes-or-no questions that ultimately lead to a classification or prediction. Decision trees is a supervised learning training model in which the training data includes labeled examples. These labels provide the algorithm with the desired output for each data point. The algorithm learns the relationship between the input features and the labels, and uses this knowledge to predict labels for new, unseen data.

Results:

Logistic Regression-                                                        
The results from the logistic regression model show that it performs well in predicting student outcomes with an overall accuracy of 91%. This means that in 91% of cases, the model correctly identified whether students would graduate or drop out.

The precision score for predicting dropouts (class 0.0) is 92%. This means that when the model predicts a student will drop out, it is correct 92% of the time. For predicting graduates (class 1.0), the precision is slightly lower at 91%. This indicates that 91% of the time the model is correct when it predicts a student will graduate.

The recall score for dropouts is 84%, indicating that the model successfully identifies 84% of the actual dropout cases. For graduates, the recall is higher at 95%, meaning the model identifies 95% of the actual graduates correctly.

The F1-score is the weighted average of precision and recall. The F1-score for predicting dropouts is 88%, and for graduates, it is 93%. These F1-scores suggest that the model has a good balance between precision and recall for both cases, with a strong performance in predicting graduates.

The model is strong, with high scores across all metrics, but it performs slightly better at identifying graduates than dropouts.

Random Forest Classifier-
Accuracy: The model has an accuracy of about 90.2%. This suggests that it correctly predicts the student's outcome (graduate or dropout) in most cases.

Precision: For predicting dropouts (class '0.0'): The precision is 91%, which means that among all the students predicted as dropouts, 91% actually did drop out. For predicting graduates (class '1.0'): The precision is 90%. This means among all the students predicted as graduates, 90% actually did graduate.

Recall: For dropouts: The recall is 83%, this means out of all the actual dropouts, the model predicts 83% correctly. For graduates: The recall is higher at 95%, indicating that the model is quite good at identifying students who will graduate.

F1-Score: For dropouts: An F1-score of 87% suggests a good balance between precision and recall for predicting dropouts. For graduates: An F1-score of 92% suggests that the balance is better for predicting graduates.

The model's performance is strong overall. The higher recall for graduates suggests that the model could be useful for identifying students at risk of not graduating, this can allow a school to provide more support to help particular students out.
