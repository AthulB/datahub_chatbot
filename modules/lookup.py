from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.util import construct_link


class QueryLookup:
    def __init__(self, df):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self.df = df

    def create_df_matrix(self):
        # create acombined vector matrix of excel data
        self.df['Combined'] = (self.df['Main'] + ' ' + self.df['Category'] + ' ' + self.df['Subcategory'] + ' ' + self.df['Questions']).astype(
            str)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['Combined'])

    # show results via user input
    def get_all_matches(self, user_input, category_filter=None):
        """Find matching links based on user input and optional category filter."""
        # convert user input to vector matrix to match it with excel data vector matrix
        user_tfidf = self.vectorizer.transform([user_input])
        cosine_similarities = cosine_similarity(user_tfidf, self.tfidf_matrix).flatten()
        # cosine similarility between both the vectors
        matched_indices = [i for i, score in enumerate(cosine_similarities) if score >= 0.25]

        if not matched_indices:
            return "Couldn't find what you are looking for, try again."

        results = []
        seen_links = set()  # To track unique links

        for idx in matched_indices:
            match = self.df.iloc[idx]

            if category_filter and match['Category'].strip().lower() != category_filter.strip().lower():
                continue

            link_name = match['Links'].strip()
            link_url = construct_link(match['Answers'].strip(), match['Page'])

            if link_name and link_url:
                cleaned_link_name = link_name.split('(')[0].strip()
                cleaned_link_url = link_url.split(' ')[0]

                if cleaned_link_url not in seen_links:
                    seen_links.add(cleaned_link_url)
                    result_entry = f"- [{cleaned_link_name}]({cleaned_link_url})"  # to show link name but redirect to link URL
                    results.append(result_entry)

        if results:
            return "This is what I found, were you looking for any of these?:\n\n" + "\n\n".join(results)
        else:
            return "Couldn't find any unique links for your query."
