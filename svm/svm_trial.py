# import numpy as np
#X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
#y = np.array([1, 1, 2, 2])
#from sklearn.svm import SVC
#clf = SVC()
#clf.fit(X, y)
#SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
#   gamma=0.0, kernel='rbf', max_iter=-1, probability=False,
#   random_state=None, shrinking=True, tol=0.001, verbose=False)
#
#print(clf.predict([[-19.0, -1]]))

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
count_vector = CountVectorizer(analyzer__min_n=1,analyzer__stop_words=set(['all', 'six', 'less', 'being', 'indeed', 'over', 'move', 'anyway', 'four', 'not', 'own', 'through', 'yourselves']))

tfidf_transformer = TfidfTransformer()

docs_new = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vector.fit_transform(docs_new)
print(X_new_counts)