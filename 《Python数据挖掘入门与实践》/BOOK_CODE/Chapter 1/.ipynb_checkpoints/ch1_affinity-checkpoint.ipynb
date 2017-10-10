{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This dataset has 100 samples and 5 features\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "dataset_filename = \"affinity_dataset.txt\"\n",
    "X = np.loadtxt(dataset_filename)\n",
    "n_samples, n_features = X.shape\n",
    "print(\"This dataset has {0} samples and {1} features\".format(n_samples, n_features))"
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
      "[[ 0.  0.  1.  1.  1.]\n",
      " [ 1.  1.  0.  1.  0.]\n",
      " [ 1.  0.  1.  1.  0.]\n",
      " [ 0.  0.  1.  1.  1.]\n",
      " [ 0.  1.  0.  0.  1.]]\n"
     ]
    }
   ],
   "source": [
    "print(X[:5])"
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
    "# The names of the features, for your reference.\n",
    "features = [\"bread\", \"milk\", \"cheese\", \"apples\", \"bananas\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In our first example, we will compute the Support and Confidence of the rule \"If a person buys Apples, they also buy Bananas\"."
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
      "36 people bought Apples\n"
     ]
    }
   ],
   "source": [
    "# First, how many rows contain our premise: that a person is buying apples\n",
    "num_apple_purchases = 0\n",
    "for sample in X:\n",
    "    if sample[3] == 1:  # This person bought Apples\n",
    "        num_apple_purchases += 1\n",
    "print(\"{0} people bought Apples\".format(num_apple_purchases))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "21 cases of the rule being valid were discovered\n",
      "15 cases of the rule being invalid were discovered\n"
     ]
    }
   ],
   "source": [
    "# How many of the cases that a person bought Apples involved the people purchasing Bananas too?\n",
    "# Record both cases where the rule is valid and is invalid.\n",
    "rule_valid = 0\n",
    "rule_invalid = 0\n",
    "for sample in X:\n",
    "    if sample[3] == 1:  # This person bought Apples\n",
    "        if sample[4] == 1:\n",
    "            # This person bought both Apples and Bananas\n",
    "            rule_valid += 1\n",
    "        else:\n",
    "            # This person bought Apples, but not Bananas\n",
    "            rule_invalid += 1\n",
    "print(\"{0} cases of the rule being valid were discovered\".format(rule_valid))\n",
    "print(\"{0} cases of the rule being invalid were discovered\".format(rule_invalid))"
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
      "The support is 21 and the confidence is 0.583.\n",
      "As a percentage, that is 58.3%.\n"
     ]
    }
   ],
   "source": [
    "# Now we have all the information needed to compute Support and Confidence\n",
    "support = rule_valid  # The Support is the number of times the rule is discovered.\n",
    "confidence = rule_valid / num_apple_purchases\n",
    "print(\"The support is {0} and the confidence is {1:.3f}.\".format(support, confidence))\n",
    "# Confidence can be thought of as a percentage using the following:\n",
    "print(\"As a percentage, that is {0:.1f}%.\".format(100 * confidence))"
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
    "from collections import defaultdict\n",
    "# Now compute for all possible rules\n",
    "valid_rules = defaultdict(int)\n",
    "invalid_rules = defaultdict(int)\n",
    "num_occurences = defaultdict(int)\n",
    "\n",
    "for sample in X:\n",
    "    for premise in range(n_features):\n",
    "        if sample[premise] == 0: continue\n",
    "        # Record that the premise was bought in another transaction\n",
    "        num_occurences[premise] += 1\n",
    "        for conclusion in range(n_features):\n",
    "            if premise == conclusion:  # It makes little sense to measure if X -> X.\n",
    "                continue\n",
    "            if sample[conclusion] == 1:\n",
    "                # This person also bought the conclusion item\n",
    "                valid_rules[(premise, conclusion)] += 1\n",
    "            else:\n",
    "                # This person bought the premise, but not the conclusion\n",
    "                invalid_rules[(premise, conclusion)] += 1\n",
    "support = valid_rules\n",
    "confidence = defaultdict(float)\n",
    "for premise, conclusion in valid_rules.keys():\n",
    "    confidence[(premise, conclusion)] = valid_rules[(premise, conclusion)] / num_occurences[premise]"
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
      "Rule: If a person buys bread they will also buy milk\n",
      " - Confidence: 0.519\n",
      " - Support: 14\n",
      "\n",
      "Rule: If a person buys milk they will also buy cheese\n",
      " - Confidence: 0.152\n",
      " - Support: 7\n",
      "\n",
      "Rule: If a person buys apples they will also buy cheese\n",
      " - Confidence: 0.694\n",
      " - Support: 25\n",
      "\n",
      "Rule: If a person buys milk they will also buy apples\n",
      " - Confidence: 0.196\n",
      " - Support: 9\n",
      "\n",
      "Rule: If a person buys bread they will also buy apples\n",
      " - Confidence: 0.185\n",
      " - Support: 5\n",
      "\n",
      "Rule: If a person buys apples they will also buy bread\n",
      " - Confidence: 0.139\n",
      " - Support: 5\n",
      "\n",
      "Rule: If a person buys apples they will also buy bananas\n",
      " - Confidence: 0.583\n",
      " - Support: 21\n",
      "\n",
      "Rule: If a person buys apples they will also buy milk\n",
      " - Confidence: 0.250\n",
      " - Support: 9\n",
      "\n",
      "Rule: If a person buys milk they will also buy bananas\n",
      " - Confidence: 0.413\n",
      " - Support: 19\n",
      "\n",
      "Rule: If a person buys cheese they will also buy bananas\n",
      " - Confidence: 0.659\n",
      " - Support: 27\n",
      "\n",
      "Rule: If a person buys cheese they will also buy bread\n",
      " - Confidence: 0.098\n",
      " - Support: 4\n",
      "\n",
      "Rule: If a person buys cheese they will also buy apples\n",
      " - Confidence: 0.610\n",
      " - Support: 25\n",
      "\n",
      "Rule: If a person buys cheese they will also buy milk\n",
      " - Confidence: 0.171\n",
      " - Support: 7\n",
      "\n",
      "Rule: If a person buys bananas they will also buy apples\n",
      " - Confidence: 0.356\n",
      " - Support: 21\n",
      "\n",
      "Rule: If a person buys bread they will also buy bananas\n",
      " - Confidence: 0.630\n",
      " - Support: 17\n",
      "\n",
      "Rule: If a person buys bananas they will also buy cheese\n",
      " - Confidence: 0.458\n",
      " - Support: 27\n",
      "\n",
      "Rule: If a person buys milk they will also buy bread\n",
      " - Confidence: 0.304\n",
      " - Support: 14\n",
      "\n",
      "Rule: If a person buys bananas they will also buy milk\n",
      " - Confidence: 0.322\n",
      " - Support: 19\n",
      "\n",
      "Rule: If a person buys bread they will also buy cheese\n",
      " - Confidence: 0.148\n",
      " - Support: 4\n",
      "\n",
      "Rule: If a person buys bananas they will also buy bread\n",
      " - Confidence: 0.288\n",
      " - Support: 17\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for premise, conclusion in confidence:\n",
    "    premise_name = features[premise]\n",
    "    conclusion_name = features[conclusion]\n",
    "    print(\"Rule: If a person buys {0} they will also buy {1}\".format(premise_name, conclusion_name))\n",
    "    print(\" - Confidence: {0:.3f}\".format(confidence[(premise, conclusion)]))\n",
    "    print(\" - Support: {0}\".format(support[(premise, conclusion)]))\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def print_rule(premise, conclusion, support, confidence, features):\n",
    "    premise_name = features[premise]\n",
    "    conclusion_name = features[conclusion]\n",
    "    print(\"Rule: If a person buys {0} they will also buy {1}\".format(premise_name, conclusion_name))\n",
    "    print(\" - Confidence: {0:.3f}\".format(confidence[(premise, conclusion)]))\n",
    "    print(\" - Support: {0}\".format(support[(premise, conclusion)]))\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rule: If a person buys milk they will also buy apples\n",
      " - Confidence: 0.196\n",
      " - Support: 9\n",
      "\n"
     ]
    }
   ],
   "source": [
    "premise = 1\n",
    "conclusion = 3\n",
    "print_rule(premise, conclusion, support, confidence, features)"
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
      "[((0, 1), 14),\n",
      " ((1, 2), 7),\n",
      " ((3, 2), 25),\n",
      " ((1, 3), 9),\n",
      " ((0, 2), 4),\n",
      " ((3, 0), 5),\n",
      " ((4, 1), 19),\n",
      " ((3, 1), 9),\n",
      " ((1, 4), 19),\n",
      " ((2, 4), 27),\n",
      " ((2, 0), 4),\n",
      " ((2, 3), 25),\n",
      " ((2, 1), 7),\n",
      " ((4, 3), 21),\n",
      " ((0, 4), 17),\n",
      " ((4, 2), 27),\n",
      " ((1, 0), 14),\n",
      " ((3, 4), 21),\n",
      " ((0, 3), 5),\n",
      " ((4, 0), 17)]\n"
     ]
    }
   ],
   "source": [
    "# Sort by support\n",
    "from pprint import pprint\n",
    "pprint(list(support.items()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from operator import itemgetter\n",
    "sorted_support = sorted(support.items(), key=itemgetter(1), reverse=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rule #1\n",
      "Rule: If a person buys cheese they will also buy bananas\n",
      " - Confidence: 0.659\n",
      " - Support: 27\n",
      "\n",
      "Rule #2\n",
      "Rule: If a person buys bananas they will also buy cheese\n",
      " - Confidence: 0.458\n",
      " - Support: 27\n",
      "\n",
      "Rule #3\n",
      "Rule: If a person buys apples they will also buy cheese\n",
      " - Confidence: 0.694\n",
      " - Support: 25\n",
      "\n",
      "Rule #4\n",
      "Rule: If a person buys cheese they will also buy apples\n",
      " - Confidence: 0.610\n",
      " - Support: 25\n",
      "\n",
      "Rule #5\n",
      "Rule: If a person buys bananas they will also buy apples\n",
      " - Confidence: 0.356\n",
      " - Support: 21\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for index in range(5):\n",
    "    print(\"Rule #{0}\".format(index + 1))\n",
    "    (premise, conclusion) = sorted_support[index][0]\n",
    "    print_rule(premise, conclusion, support, confidence, features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "sorted_confidence = sorted(confidence.items(), key=itemgetter(1), reverse=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rule #1\n",
      "Rule: If a person buys apples they will also buy cheese\n",
      " - Confidence: 0.694\n",
      " - Support: 25\n",
      "\n",
      "Rule #2\n",
      "Rule: If a person buys cheese they will also buy bananas\n",
      " - Confidence: 0.659\n",
      " - Support: 27\n",
      "\n",
      "Rule #3\n",
      "Rule: If a person buys bread they will also buy bananas\n",
      " - Confidence: 0.630\n",
      " - Support: 17\n",
      "\n",
      "Rule #4\n",
      "Rule: If a person buys cheese they will also buy apples\n",
      " - Confidence: 0.610\n",
      " - Support: 25\n",
      "\n",
      "Rule #5\n",
      "Rule: If a person buys apples they will also buy bananas\n",
      " - Confidence: 0.583\n",
      " - Support: 21\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for index in range(5):\n",
    "    print(\"Rule #{0}\".format(index + 1))\n",
    "    (premise, conclusion) = sorted_confidence[index][0]\n",
    "    print_rule(premise, conclusion, support, confidence, features)"
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
