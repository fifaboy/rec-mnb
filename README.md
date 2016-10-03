# This work is copyrighted. Publishing or using any portion of this research without any consent is strictly forbidden.

## Datasets
* CiaoDVD
* filmtrust
* Movielens rating dataset (a CSV file)
* Other datasets here: http://librec.net/datasets.html
* Site for recommender systems: http://www.recsyswiki.com/wiki/Main_Page

## Language
* C++ (unlikely to use)
* Python

## Packages
Install the following packages on a linux machine. You can install them in two ways: sudo pip3 install numpy or sudo apt-get install python-numpy. Choose the method whichever works fine. They are necessary for testing accuracy and will be used for prediction as well. Moreover, they make our lives a lot easier in terms of coding.
* numpy
* scipy
* scikit-learn
* matplotlib
* pandas
* jupyter
* ipython
* conda

## Approach (Will be updated from time to time)
* Learning on weights
* Polynomial Regression
* Naive Bayes (multinomialNB)

## Testing Accuracy
We will use:
* 80% data for training and 20% for testing
* 5-fold cross validation system
Rating prediction in two ways if possible:
* Collaborative filtering and finding similar users
* Prediction only using the user ratings alone

### How to Collaborate
* Always work on your branch only
* Push only when the work is done for sure, so there is no bad merge
* Maintain this workflow:
* checkout master
* pull master
* merge with master
* push your branch and start working
* when done, commit and push in your branch
* merge with master only when a feature is done
* push master
* checkout your branch again
* Summary: always stay in your branch. DO NOT stay in master even when you are not working. This results in conflicts
* If there are still any conflicts, delete swp or merge files from .git (search in google first). Be sure to save your work and keep the remote repo safe at least.
* If there is a prompt for merge message, press ESC+Shift+Z (twice) all at the same time. It will exit merge message prompt and just do it.
* If there is any problem, let me know. And if you are not sure, do not merge.
