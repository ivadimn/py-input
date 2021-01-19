from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns

corpus = [
    "Time flies like an arrow",
    "Fruit flies like a banana" ]

vocab = ["an", "arrow", "banana", "flies", "fruit", "like", "time"]
one_hot_vectorizer = CountVectorizer(binary=True)
one_hot = one_hot_vectorizer.fit_transform(corpus).toarray()
sns.heatmap(one_hot, annot=True, cbar=False, xticklabels=vocab, yticklabels=["Предложение 1", "Предложение 2"])
