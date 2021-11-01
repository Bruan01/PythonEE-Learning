score=open(r'/score.txt', 'r', encoding='utf-8')
read_lines=score.readlines()
score.close()
##print(read_lines)
for i in read_lines:
    data=i.split()
    ##print(data)
    sum = 0
    for scores in data[1:]:
        sum=sum +int (scores)
    result = data[0]+str(sum)+'\n'
    print(result)
    final_scores = []
    final_scores.append(result)
    
winner = open(r'/winner.txt', 'w', encoding='utf-8')
for i in final_scores:
    winner.writelines(i)
winner.close()
