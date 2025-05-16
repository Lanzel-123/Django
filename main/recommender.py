import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Example dataset
data = {
    'item_id': [1, 2, 3, 4],
    'title': ['Django for Beginners', 'Advanced Django', 'Python Basics', 'Machine Learning Intro'],
    'description': [
        'Learn Django step-by-step',
        'Deep dive into Django framework',
        'Basic Python programming concepts',
        'Introduction to ML concepts'
    ]
}

df = pd.DataFrame(data)

# Create TF-IDF matrix from descriptions
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Calculate similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, cosine_sim=cosine_sim):
    # Find index of the item that matches the title
    idx = df.index[df['title'] == title][0]
    
    # Get pairwise similarity scores for that item with all others
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort by similarity score, highest first
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get scores of 2 most similar items (excluding itself)
    sim_scores = sim_scores[1:3]
    
    # Get item indices
    item_indices = [i[0] for i in sim_scores]
    
    # Return titles of recommended items
    return df['title'].iloc[item_indices].tolist()

# Example usage
if __name__ == "__main__":
    print(get_recommendations('Django for Beginners'))
