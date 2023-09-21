first_score = int(input("Enter first score: ")) # 0
second_score = int(input("Enter second score: ")) # 1
third_score = int(input("Enter third score: ")) # 2
# put ashley's scores in a list
a_list = [first_score, second_score, third_score]

# ask for barb's scores
first_score = int(input("Enter first score: "))
second_score = int(input("Enter second score: "))
third_score = int(input("Enter third score: "))
# put barb's scores in a list
b_list = [first_score, second_score, third_score]

# ask for carl's scores
first_score = int(input("Enter first score: "))
second_score = int(input("Enter second score: "))
third_score = int(input("Enter third score: "))
# put carl's scores in a list
c_list = [first_score, second_score, third_score]

all_scores = [a_list[:], b_list[:], c_list[:]]
print("All Scores: ", all_scores)
new_list = []
for each_list in all_scores:
    score_list = []
    for each_score in each_list:
        new_score = int(each_score * 1.05)
        score_list.append(new_score)
    new_list.append(score_list)
print("All Scores after credit increase: ", new_list)

score_spread = []
for each_list in new_list:
    score_spread.append(max(each_list) - min(each_list))
print("Score spread: ", score_spread)

print("Original scores")
print("Ashley: ", a_list)
print("Barb: ", b_list)
print("Carl: ", c_list)