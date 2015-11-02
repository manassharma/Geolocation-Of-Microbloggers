from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

native_users = []
input_location  = "BurbankCA_Standardized.txt"
with open(input_location, 'r') as user_inf:
    for line in user_inf:
        user_details = line.split('\t')
        native_user_id = user_details[0]
        native_users.append(native_user_id)

native_users_list = list(set(native_users))
no_of_native_users = len(native_users_list)
similarity_matrix = [[0] * no_of_native_users] * no_of_native_users


def compute_cosine_similarity(user1, user2):
    global similarity_matrix
    user1_file_loc = "/Users/agalya/Documents/education/fall_15/projects/community_analysis/com1/user_tweets/" + user1 + ".txt"
    user2_file_loc = "/Users/agalya/Documents/education/fall_15/projects/community_analysis/com1/user_tweets/" + user2 + ".txt"
    tweets_grouped_by_users = [user1_file_loc]

    tweets_grouped_by_users.insert(0, user2_file_loc)
    user_tweets = [open(user_tweets) for user_tweets in tweets_grouped_by_users]
    tfidf_files = TfidfVectorizer(input='file').fit_transform(user_tweets)
    return cosine_similarity(tfidf_files[0], tfidf_files[1])[0][0]

similarity_values = []
for i in range(0, no_of_native_users):
    for j in range(i + 1, no_of_native_users):
        try:
            user_id_1 = native_users_list[i]
            user_id_2 = native_users_list[j]
            similarity = compute_cosine_similarity(user_id_1, user_id_2)
            similarity_matrix[i][j] = similarity
            if similarity != 0:
                similarity_values.append(float("{0:.1f}".format(similarity)))
        except:
            similarity_matrix[i][j] = 0
            print("Error parsing the native user " + user_id_1 + " with user " + user_id_2)

print(similarity_matrix)
similarity_file = open("similarity_matrix" + input_location+ ".txt", 'a')
similarity_file.write(str(similarity_matrix))
similarity_file.close()
average_similarity_value = sum(similarity_values) / len(similarity_values)
freq_similarity_value = Counter(similarity_values).most_common()

output = open("similarity" + input_location + ".txt", 'a')
output.write("Average similarity value for " + input_location + " is : " + str(average_similarity_value))
output.write('\n')
output.write("Most frequent similarity value for " + input_location + " is : " + str(freq_similarity_value))
output.write('\n')
output.close()
