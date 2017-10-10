{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The OneR algorithm is quite simple but can be quite effective, showing the power of using even basic statistics in many applications.\n",
    "The algorithm is:\n",
    "\n",
    "* For each variable\n",
    "    * For each value of the variable\n",
    "        * The prediction based on this variable goes the most frequent class\n",
    "        * Compute the error of this prediction\n",
    "    * Sum the prediction errors for all values of the variable\n",
    "* Use the variable with the lowest error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Iris Plants Database\n",
      "\n",
      "Notes\n",
      "-----\n",
      "Data Set Characteristics:\n",
      "    :Number of Instances: 150 (50 in each of three classes)\n",
      "    :Number of Attributes: 4 numeric, predictive attributes and the class\n",
      "    :Attribute Information:\n",
      "        - sepal length in cm\n",
      "        - sepal width in cm\n",
      "        - petal length in cm\n",
      "        - petal width in cm\n",
      "        - class:\n",
      "                - Iris-Setosa\n",
      "                - Iris-Versicolour\n",
      "                - Iris-Virginica\n",
      "    :Summary Statistics:\n",
      "    ============== ==== ==== ======= ===== ====================\n",
      "                    Min  Max   Mean    SD   Class Correlation\n",
      "    ============== ==== ==== ======= ===== ====================\n",
      "    sepal length:   4.3  7.9   5.84   0.83    0.7826\n",
      "    sepal width:    2.0  4.4   3.05   0.43   -0.4194\n",
      "    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)\n",
      "    petal width:    0.1  2.5   1.20  0.76     0.9565  (high!)\n",
      "    ============== ==== ==== ======= ===== ====================\n",
      "    :Missing Attribute Values: None\n",
      "    :Class Distribution: 33.3% for each of 3 classes.\n",
      "    :Creator: R.A. Fisher\n",
      "    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)\n",
      "    :Date: July, 1988\n",
      "\n",
      "This is a copy of UCI ML iris datasets.\n",
      "http://archive.ics.uci.edu/ml/datasets/Iris\n",
      "\n",
      "The famous Iris database, first used by Sir R.A Fisher\n",
      "\n",
      "This is perhaps the best known database to be found in the\n",
      "pattern recognition literature.  Fisher's paper is a classic in the field and\n",
      "is referenced frequently to this day.  (See Duda & Hart, for example.)  The\n",
      "data set contains 3 classes of 50 instances each, where each class refers to a\n",
      "type of iris plant.  One class is linearly separable from the other 2; the\n",
      "latter are NOT linearly separable from each other.\n",
      "\n",
      "References\n",
      "----------\n",
      "   - Fisher,R.A. \"The use of multiple measurements in taxonomic problems\"\n",
      "     Annual Eugenics, 7, Part II, 179-188 (1936); also in \"Contributions to\n",
      "     Mathematical Statistics\" (John Wiley, NY, 1950).\n",
      "   - Duda,R.O., & Hart,P.E. (1973) Pattern Classification and Scene Analysis.\n",
      "     (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.\n",
      "   - Dasarathy, B.V. (1980) \"Nosing Around the Neighborhood: A New System\n",
      "     Structure and Classification Rule for Recognition in Partially Exposed\n",
      "     Environments\".  IEEE Transactions on Pattern Analysis and Machine\n",
      "     Intelligence, Vol. PAMI-2, No. 1, 67-71.\n",
      "   - Gates, G.W. (1972) \"The Reduced Nearest Neighbor Rule\".  IEEE Transactions\n",
      "     on Information Theory, May 1972, 431-433.\n",
      "   - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al\"s AUTOCLASS II\n",
      "     conceptual clustering system finds 3 classes in the data.\n",
      "   - Many, many more ...\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Load our dataset\n",
    "from sklearn.datasets import load_iris\n",
    "#X, y = np.loadtxt(\"X_classification.txt\"), np.loadtxt(\"y_classification.txt\")\n",
    "dataset = load_iris()\n",
    "X = dataset.data\n",
    "y = dataset.target\n",
    "print(dataset.DESCR)\n",
    "n_samples, n_features = X.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Our attributes are continuous, while we want categorical features to use OneR. We will perform a *preprocessing* step called discretisation. At this stage, we will perform a simple procedure: compute the mean and determine whether a value is above or below the mean."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Compute the mean for each attribute\n",
    "attribute_means = X.mean(axis=0)\n",
    "assert attribute_means.shape == (n_features,)\n",
    "X_d = np.array(X >= attribute_means, dtype='int')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are (112,) training samples\n",
      "There are (38,) testing samples\n"
     ]
    }
   ],
   "source": [
    "# Now, we split into a training and test set\n",
    "from sklearn.cross_validation import train_test_split\n",
    "\n",
    "# Set the random state to the same number to get the same results as in the book\n",
    "random_state = 14\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X_d, y, random_state=random_state)\n",
    "print(\"There are {} training samples\".format(y_train.shape))\n",
    "print(\"There are {} testing samples\".format(y_test.shape))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from collections import defaultdict\n",
    "from operator import itemgetter\n",
    "\n",
    "\n",
    "def train(X, y_true, feature):\n",
    "    \"\"\"Computes the predictors and error for a given feature using the OneR algorithm\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    X: array [n_samples, n_features]\n",
    "        The two dimensional array that holds the dataset. Each row is a sample, each column\n",
    "        is a feature.\n",
    "    \n",
    "    y_true: array [n_samples,]\n",
    "        The one dimensional array that holds the class values. Corresponds to X, such that\n",
    "        y_true[i] is the class value for sample X[i].\n",
    "    \n",
    "    feature: int\n",
    "        An integer corresponding to the index of the variable we wish to test.\n",
    "        0 <= variable < n_features\n",
    "        \n",
    "    Returns\n",
    "    -------\n",
    "    predictors: dictionary of tuples: (value, prediction)\n",
    "        For each item in the array, if the variable has a given value, make the given prediction.\n",
    "    \n",
    "    error: float\n",
    "        The ratio of training data that this rule incorrectly predicts.\n",
    "    \"\"\"\n",
    "    # Check that variable is a valid number\n",
    "    n_samples, n_features = X.shape\n",
    "    assert 0 <= feature < n_features\n",
    "    # Get all of the unique values that this variable has\n",
    "    values = set(X[:,feature])\n",
    "    # Stores the predictors array that is returned\n",
    "    predictors = dict()\n",
    "    errors = []\n",
    "    for current_value in values:\n",
    "        most_frequent_class, error = train_feature_value(X, y_true, feature, current_value)\n",
    "        predictors[current_value] = most_frequent_class\n",
    "        errors.append(error)\n",
    "    # Compute the total error of using this feature to classify on\n",
    "    total_error = sum(errors)\n",
    "    return predictors, total_error\n",
    "\n",
    "# Compute what our predictors say each sample is based on its value\n",
    "#y_predicted = np.array([predictors[sample[feature]] for sample in X])\n",
    "    \n",
    "\n",
    "def train_feature_value(X, y_true, feature, value):\n",
    "    # Create a simple dictionary to count how frequency they give certain predictions\n",
    "    class_counts = defaultdict(int)\n",
    "    # Iterate through each sample and count the frequency of each class/value pair\n",
    "    for sample, y in zip(X, y_true):\n",
    "        if sample[feature] == value:\n",
    "            class_counts[y] += 1\n",
    "    # Now get the best one by sorting (highest first) and choosing the first item\n",
    "    sorted_class_counts = sorted(class_counts.items(), key=itemgetter(1), reverse=True)\n",
    "    most_frequent_class = sorted_class_counts[0][0]\n",
    "    # The error is the number of samples that do not classify as the most frequent class\n",
    "    # *and* have the feature value.\n",
    "    n_samples = X.shape[1]\n",
    "    error = sum([class_count for class_value, class_count in class_counts.items()\n",
    "                 if class_value != most_frequent_class])\n",
    "    return most_frequent_class, error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The best model is based on variable 2 and has error 37.00\n",
      "{'variable': 2, 'predictor': {0: 0, 1: 2}}\n"
     ]
    }
   ],
   "source": [
    "# Compute all of the predictors\n",
    "all_predictors = {variable: train(X_train, y_train, variable) for variable in range(X_train.shape[1])}\n",
    "errors = {variable: error for variable, (mapping, error) in all_predictors.items()}\n",
    "# Now choose the best and save that as \"model\"\n",
    "# Sort by error\n",
    "best_variable, best_error = sorted(errors.items(), key=itemgetter(1))[0]\n",
    "print(\"The best model is based on variable {0} and has error {1:.2f}\".format(best_variable, best_error))\n",
    "\n",
    "# Choose the bset model\n",
    "model = {'variable': best_variable,\n",
    "         'predictor': all_predictors[best_variable][0]}\n",
    "print(model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def predict(X_test, model):\n",
    "    variable = model['variable']\n",
    "    predictor = model['predictor']\n",
    "    y_predicted = np.array([predictor[int(sample[variable])] for sample in X_test])\n",
    "    return y_predicted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 0 0 2 2 2 0 2 0 2 2 0 2 2 0 2 0 2 2 2 0 0 0 2 0 2 0 2 2 0 0 0 2 0 2 0 2\n",
      " 2]\n"
     ]
    }
   ],
   "source": [
    "y_predicted = predict(X_test, model)\n",
    "print(y_predicted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The test accuracy is 65.8%\n"
     ]
    }
   ],
   "source": [
    "# Compute the accuracy by taking the mean of the amounts that y_predicted is equal to y_test\n",
    "accuracy = np.mean(y_predicted == y_test) * 100\n",
    "print(\"The test accuracy is {:.1f}%\".format(accuracy))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from sklearn.metrics import classification_report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             precision    recall  f1-score   support\n",
      "\n",
      "          0       0.94      1.00      0.97        17\n",
      "          1       0.00      0.00      0.00        13\n",
      "          2       0.40      1.00      0.57         8\n",
      "\n",
      "avg / total       0.51      0.66      0.55        38\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/usr/local/lib/python3.4/dist-packages/sklearn/metrics/metrics.py:1771: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples.\n",
      "  'precision', 'predicted', average, warn_for)\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(y_test, y_predicted))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
