def learn_perceptron(weights, bias, training_examples, learning_rate, 
                     max_epochs):
    for epoch in range(1, max_epochs + 1):
        # print("-" * 20, "epoch:", epoch, 20 * "-")
        # print("weights: ", weights)
        # print("bias: ", bias)
        seen_error = False
        for input, target in training_examples:
            # a = 
            # output = 
            # print("input: {} output: {} target: {}".format(
            #    input, output, target))
            if output != target:
                seen_error = True
                # Now update the weights and bias
                # weights = 
                # bias = 
                # print("updating the weights and bias to: ", weights, bias)

        if not seen_error:
            def perceptron(input_vector):
                # a = 
                # output = 
                return output
            return perceptron;;