           # игр % побед #болельщиков
weights = [ [0.1, 0.1, -0.3], # травмы?
            [0.1, 0.2, 0.0],  # победа?
            [0.0, 1.3, 0.1] ] # печаль?
def neural_network(input, weights):
    assert (len(input) == len(weights))
    output_cures_wins_sad = []
    for element in weights:
        output = 0
        for i in range(len(element)):
            output += element[i] * input[i] # каждой самостоятельной вероятности
        output_cures_wins_sad.append(output)
    return output_cures_wins_sad
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

for element in range(len(toes)):
    main_list = [toes[element], wlrec[element], nfans[element]]
    pred_answer = neural_network(main_list, weights)
    print("The result of {0} games, {1} win/lose, {2} fans is equal to \n {3} to get a cure \n {4} to win \n and {5} "
          "to be sad".format(round(toes[element],4), round(wlrec[element],4) , round(nfans[element], 4),
                             round(pred_answer[0], 4), round(pred_answer[1], 4), round(pred_answer[2], 4)))

