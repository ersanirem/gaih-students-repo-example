#Question 1; How would you define Machine Learning
The system learns its past experiences with the model it has developed using its data.
Ability to use this knowledge on new data without the need for reprogramming for future tasks.



#Question 2; What are the differences between Supervised and Unsupervised Learning? Specify example 3 algorithms for each of these. 
 Supervised Learnig is a approach that here the program is given labeled input data and the expected output results.But in unsupervised learning, 
we have unlabeled training data.
 For example;
  1- Image classification. We can use supervised learning to check if it is a dog or a cat in the picture.
  2- Predicting next year's sales volume
  3- Checking an email if it is spam or not spam
  For unsupervised learning examples;
  1-Clustering DNA patterns to analyze evolutionary biology.
  2-Recommender systems - giving better Amazon purchase suggestions or Netflix movie matches
  3-Medical imaging - for distinguishing between different kinds of tissues
  
  
  
 #Question 3; What are the test and validation set, and why would you want to use them?
 – Training set: A set of examples used for learning, that is to fit the parameters of the classifier.
 –  Validation set: A set of examples used to tune the parameters of a classifier, for example to choose the number of hidden units in a neural network.
 It is usually used for parameter selection and to avoid overfitting
 – Test set: The sample of data used to provide an unbiased evaluation of a final model fit on the training dataset.
  
In order to reach a good and effective algorithm, to make accurate and true predictions we should use validation and test test.
Because we can avoid overfitting with use of validation test.And with test set we can see the accuracy of our model and see how good it works.



#Question 4; What are the main preprocessing steps? Explain them in detail. Why we need to prepare our data? 
#Why we need to prepare our data? 
In Data preparation, we load our data into a suitable place and prepare it for use in our machine learning training. 
It is important because we can see if there are any relevant relationships between different variables you can take advantage of, 
as well as if there are any data imbalances. It is essential to identify these outliers, duplicated values etc. Because it will affect our algorithm in a negative way.
#What are the main preprocessing steps?
  1. Acquire the dataset; To build and develop Machine Learning models, we must first acquire the relevant dataset. 
 This dataset will be comprised of data gathered from multiple and disparate sources which are then combined in a proper format to form a dataset. 
  2. Import all the crucial libraries; like NumPy, MatPlobLib, Pandas. These are very beneficial for importing, managing datasets.
  3. Import the dataset; In this step, we need to import the dataset/s that we have gathered for the ML project at hand
  4. Identifying and handling the missing values; 
  We can eleminate missing values or fill them with mean or median.
 If we dont handle missing values, we can get inaccurate values. 
  5. Encoding the categorical data;
  Categorical data refers to the information that has specific categories within the dataset. 
  Machine Learning models are primarily based on mathematical equations. 
  Thus, we can intuitively understand that keeping the categorical data in the equation will cause certain issues since we would only need numbers in the equations.
  6. Splitting the dataset; Every dataset for Machine Learning model must be split into two separate sets – training set and test set. 
  Usually, the dataset is split into 70:30 ratio or 80:20 ratio.
  7. Feature scaling; Feature scaling marks the end of the data preprocessing in Machine Learning. 
  It is a method to standardize the independent variables of a dataset within a specific range.
  In other words, feature scaling limits the range of variables so that we can compare them on common grounds.
  We can perform feature scaling in Machine Learning in two ways; Standardization and Normalization.
  
  
  
  
  #Question 5;How you can explore and analyse countionus and discrete variables?
  Discrete data involves round, concrete numbers that are determined by counting.
  Continuous data involves complex numbers that are measured across a specific time interval.
  A simple way to describe the difference between the two is to visualize a scatter plot graph vs. a line graph.
  We can explore and analyse them by drawing a scatter plot and line graph. We can see more clearly by visualizing.
  
  
  #Question 6; Analyse the plot given below. (What is the plot and variable type, check the distribution and make comment about how you can preproccess it.)
  This is a  MatPlobLib histogram. 
  Continuous variable.
  We use histogram to analyse continuous variable. 
   If the graph is approximately bell-shaped and symmetric about the mean, we can usually assume normality.
   But we dont see this shape, so it is not normal distribution. Our ditribution is really asymmetric.
   It is not also right skewed right or left. We can say it has a random distribution.It has no apparent pattern.
   We can check if there is a outlier around 0-1 petal width. Because there is a anormal value compared to others.
   
   
  
  
  
  
  
  
  
  
  
  
  
  
  
