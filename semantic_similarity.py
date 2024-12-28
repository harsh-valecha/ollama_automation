from sentence_transformers import SentenceTransformer, util

# Load a pre-trained Sentence Transformer model
# Load the model
# model = SentenceTransformer('all-MiniLM-L6-v2')
# model.save('semantic_similarity/')
model = SentenceTransformer('semantic_similarity/')

# Texts to compare
text1 = "The sky is blue because of light scattering."
text2 = '''
The reason why sky blue appears to be blue, rather than green or gray, is due to the way that light reflects and refracts
 on the surface of the Earth. Blue wavelengths of light are reflected first by polarized sunlight, which gives the blue color to clouds in the sky. 
These reflections occur because blue light has a longer wavelength than green and red light. Additionally, as light travels through the atmosphere, 
it is scattered by tiny particles called droplets or ice crystals, which produce a rainbow-like pattern of colors in the upper atmosphere called a "cloud" or "rainbow."

When sunlight hits these droplets, they reflect blue light and emit other colors such as green or red. The scattering effect is what gives the sky i
ts distinctive hue. In fact, the term "sky blue" simply means that the color appears blue to our eyes from Earth's vantage point. However, in many c
ases of photographic blue shading (i.e., when the colors seem darker or lighter than they really are), the droplets and particles causing the scattering are not visible on the ground.

So while sky blue is a beautiful color, it is not a unique characteristic of the sky but merely an effect that can be caused by the scattering of sunlight by tiny droplets in the air.
'''

# Convert texts to embeddings
embedding1 = model.encode(text1, convert_to_tensor=True)
embedding2 = model.encode(text2, convert_to_tensor=True)

# Calculate cosine similarity
similarity = util.cos_sim(embedding1, embedding2)


print(f"Semantic Similarity: {similarity.item():.2f}")

