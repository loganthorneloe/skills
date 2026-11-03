# Coverage questions — transformer attention (frozen before generation)
Score each 0/1/2 from the report alone. 2 = a novice reading only this report could answer correctly; 1 = partial, implicit, or needs inference the report does not support; 0 = missing or wrong.
Q1. How is text represented before attention? Key: text is split into tokens, each mapped to a vector (embedding), with position information added.
Q2. What problem does attention solve? Key: a word's meaning depends on other words in context; each position needs to gather relevant information from other positions.
Q3. What are queries, keys and values? Key: three learned linear projections (matrix multiplications) of each token vector; query = what I'm looking for, key = what I offer for matching, value = information passed along.
Q4. Walk through the computation. Key: scores = Q·Kᵀ (dot products), scaled by √d, softmax turns each row into weights summing to 1, output = weighted sum of V vectors.
Q5. Why multiple heads? Key: several attention computations with different projections in parallel let the model track different relationships; outputs are concatenated and projected.
Q6. How does a language model use it to generate text? Key: causal masking so a token attends only to earlier tokens; stacked layers; predict next token; trained on large text to minimize prediction error.
Q7. Why did it enable large models like ChatGPT? Key: unlike recurrent networks it processes all positions in parallel, making training on GPUs efficient at scale, and connects distant tokens directly; scaling data/parameters improved performance.
Q8 (transfer). What is attention's main cost as context grows, and why? Key: every token scores against every other token, so compute and memory grow quadratically with sequence length.
