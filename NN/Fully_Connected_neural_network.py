inputs = [1,2,3,4]
# weights associted with this are 
weights = [ [0.2, 0.8, -0.5, 1],
          [0.33, -0.31, -0.7, ],
          [1.1,2.9,-0.1,-2.3],
          [0.5, -0.91, 0.26, -0.5] ]

biases = [2, 3, 0.5,1]
# Output of current layer
layers_output = []

layer_outputs = []
# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
        neuron_output += neuron_bias

layer_outputs.append(neuron_output)
print(layer_outputs)