from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_predictor(df):
    df = df.dropna()
    df['MACD'] = df['Close'].ewm(12).mean() - df['Close'].ewm(26).mean()
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)

    features = df[['RSI', 'MACD', 'Volume']].dropna()
    labels = df['Target'].loc[features.index]
    
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, shuffle=False)

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, clf.predict(X_test))
    return clf, accuracy
