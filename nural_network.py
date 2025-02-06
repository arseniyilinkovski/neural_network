class NeuralNetwork:
    def get_result(self, inp: list, weights: list):
        prediction_h = [0] * len(weights[0])
        for i in range(len(weights[0])):
            ws = 0
            for j in range(len(inp)):
                ws += inp[j] * weights[0][i][j]
            prediction_h[i] = ws

        prediction_out = [0] * len(weights[1])
        i, j = 0, 0
        for i in range(len(weights[1])):
            ws = 0
            for j in range(len(prediction_h)):
                ws += prediction_h[j] * weights[1][i][j]
            prediction_out[i] = ws
        return prediction_out




inp = [50, 165]

weights_h_1 = [0.2, 0.1]
weights_h_2 = [0.3, 0.1]

weights_out_1 = [0.4, 0.2]
weights_out_2 = [0.5, 0.3]

weights_h = [weights_h_1, weights_h_2]
weights_out = [weights_out_1, weights_out_2]
weights = [weights_h, weights_out]


neural_network = NeuralNetwork()
print(neural_network.get_result(inp, weights))
