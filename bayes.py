from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def convert(data):
    ids = []
    length = len(data)
    users = data['user_id'].values
    movies = data['movie_id'].values
    for i in range(0, length):
        ids.append(str(users[i])+' '+str(movies[i]))
    return ids
def predict(train_data, test_data):
    vectorizer = CountVectorizer()
    train_ids = []
    #length = len(train_data['user_id'])
    train_ids = convert(train_data)
    inputs = vectorizer.fit_transform(train_ids)
    classifier = MultinomialNB()
    outputs = train_data['rating'].values
    classifier.fit(inputs, outputs)
    test_ids = convert(test_data)
    test = vectorizer.transform(test_ids)
    predictions = classifier.predict(test)
    return predictions
