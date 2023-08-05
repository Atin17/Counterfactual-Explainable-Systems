import pickle
sentiment_data = []  # [userID, itemID, [fos triplet 1], [fos triplet 2], ...]
sentires_file = "/common/home/ps1279/PycharmProjects/pythonProject/Sentires-Guide/English-Jar/lei/output/reviews.pickle"
if len(sentires_file.split(".")) > 0 and sentires_file.split(".")[-1] == "pickle":
    with open(sentires_file,
              'rb') as ip:
        pickle_data = pickle.load(ip)

    for item in pickle_data:
        if 'sentence' in item:
            sent_entries = item['sentence']
            temp_sent_data = [item["user"], item["item"]]

            for each_sent in sent_entries:
                sign = each_sent[3]
                if sign == 1:
                    sign = "+1"
                elif sign == -1:
                    sign = "-1"
                temp_sent_data.append([each_sent[0], each_sent[1], sign])
            sentiment_data.append(temp_sent_data)
print('hello')