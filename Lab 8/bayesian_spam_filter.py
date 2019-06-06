import csv

def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    true_count = pseudo_count
    false_count = pseudo_count
    for row in training_examples[1:]:
        if int(row[-1]):
            true_count += 1
        else:
            false_count += 1

    return (true_count) / (true_count + false_count)


def learn_likelihood(file_name, pseudo_count=0):
    
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    counts = []
    for i in range(len(training_examples[0]) - 1):
        counts.append([pseudo_count, pseudo_count])
    spam_true = pseudo_count# * (len(training_examples[0]) - 1) 
    spam_false = pseudo_count# * (len(training_examples[0]) - 1)
    
    for row in training_examples[1:]:
        for index, value in enumerate(row[:-1]):
            #print(index)
            if int(value):
                counts[index][int(row[-1])] += 1
            #else:
            #    counts[index][False] += 1
        if int(row[-1]):
            spam_true += 1
        else:
            spam_false += 1
                
    #prob_spam = learn_prior(file_name, pseudo_count)
    
    likelihoods = []
    #print(counts)
    for feature_given_false, feature_given_true in counts:
        #print(feature_give_false, feature_give_true)
        #prob_feature = true_count / (true_count + false_count)
        true_prob = feature_given_true / (spam_true + pseudo_count)#prob_feature given Spam = True
        false_prob = feature_given_false / (spam_false  + pseudo_count)
        likelihoods.append((false_prob, true_prob))
    
    return likelihoods

def posterior(prior, likelihood, observation):
    """Returns the posterior probability of the class variable being true, given
       the observation, ie. it returns p(Class=true|observation). The argument
       observation is a tuple of n booleans such that observation[i] is the
       observed value (T/F) for the input feature X[i]. Prior = a real number
       representing p(Class=true). likelihood = a tuple of length n where each
       element is a pair of real numbers such that 
       likelihood[i][False] = p(X[i]=true|C=false) and
       likelihood[i][True] = p(X[i]=true|C=true)."""
    prior_f = 1 - prior
    features_true = 1
    features_false = 1
    for i in range(len(observation)):
        if observation[i]:
            features_true *= likelihood[i][True]
            features_false *= likelihood[i][False]
        else:
            features_true *= 1 - likelihood[i][True]
            features_false *= 1 - likelihood[i][False]
    features_true *= prior
    features_false *= prior_f
    
    return features_true / (features_true + features_false)


def nb_classify(prior, likelihood, input_vector):
    prob_spam = posterior(prior, likelihood, input_vector)
    prob_not_spam = 1 - prob_spam
    if prob_spam > prob_not_spam:
        return ("Spam", prob_spam)
    elif prob_spam < prob_not_spam:
        return ("Not Spam", prob_not_spam)
    else:
        return ("Not Spam", prob_not_spam)
    
    
def accuracy(predicted_labels, correct_labels):
    num_correct = 0
    num_guesses = len(correct_labels)
    for i in range(num_guesses):
        if predicted_labels[i] == correct_labels[i]:
            num_correct += 1
    return num_correct / num_guesses