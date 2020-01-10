# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:35:50 2019

@author: breese
"""
from nltk.corpus import ppattach
from nltk.stem.porter import PorterStemmer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder


stemmer = PorterStemmer()

#Scikit-learn vectorizers and label encoders 
vec = DictVectorizer()
le = LabelEncoder()


# DATA: raw training and test data
train = ppattach.attachments('training')
test = ppattach.attachments('test')



# COMPLETE THE FEATURE EXTRACTOR FUNCTION!  This function should
# return a list of true labels and list of feature dictionaries. You only
# have to edit the portion of the function that extracts feature-value pairs
# from corpus instances.  
def featureExtractor(data):
    feature_dicts = []
    labels = []
    for i in data:
        labels.append(i.attachment)
        features = {}
        # Extract feature-value pairs:
        features['verb'] = i.verb
        features['verb+prep'] = stemmer.stem(i.verb) + " " +  i.prep
        # ADD AT LEAST FIVE NEW FEATURES:
        features['noun1'] = i.noun1
        features['noun2'] = i.noun2
        features['prep'] = i.prep
        features['noun1+prep'] = i.noun1 + " " + i.prep
        features['noun2+prep'] = i.noun2 + " " + i.prep
        
        # Feature to improve classification accuracy
        features['pluralnoun1'] = i.noun1[len(i.noun1)-1] == 's'

        # Append feature dictionary to dictionary list:
        feature_dicts.append(features)
    return (feature_dicts, labels)



# Call the featureExtractor function to get feature representations of 
# the train and test data.    
X_train, y_train = featureExtractor(train)
X_test, y_test = featureExtractor(test)


# Transform data to numeric representations using vectorizer and label
# encoder.
r = len(X_train)

X = X_train + X_test
X = vec.fit_transform(X)
X_train = X[:r,:]
X_test = X[r:,:]

y_train = le.fit_transform(y_train)
y_test = le.fit_transform(y_test)


# Instantiate Maxent classifier:
clf = LogisticRegression(random_state=0,
                         solver='lbfgs',
                         max_iter=1000,
                         multi_class='multinomial')

# Train the classifier:
clf.fit(X_train, y_train)

# Apply classifier to test data and evaluate.
y_pred = clf.predict(X_test)

print("Classification accuracy: {:.2f}".format(accuracy_score(y_test, y_pred)))
print("\n")
print(classification_report(y_test, y_pred, target_names=le.classes_))
