inputs_x  = [2,4,5]
# weigth and bias are the tunable paramters in neural networks
weights_w = [1.1, 2.49, 1.33]

bias = 2

outputs = ( inputs_x[0]*weights_w[0] + 
            inputs_x[1]*weights_w[1] +
             inputs_x[2]*weights_w[2] + bias

        )

print(outputs)
