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