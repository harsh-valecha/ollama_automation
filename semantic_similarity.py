from sentence_transformers import SentenceTransformer, util

# Load a pre-trained Sentence Transformer model
# Load the model
# model = SentenceTransformer('all-MiniLM-L6-v2')
# model.save('semantic_similarity/')
model = SentenceTransformer('semantic_similarity/')

# Texts to compare
text1 = "The sky is blue because of light scattering."
text2 = "Light scattering causes the sky to appear blue."

# Convert texts to embeddings
embedding1 = model.encode(text1, convert_to_tensor=True)
embedding2 = model.encode(text2, convert_to_tensor=True)

# Calculate cosine similarity
similarity = util.cos_sim(embedding1, embedding2)


print(f"Semantic Similarity: {similarity.item():.2f}")

