from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer

# Select model
tokenizer = Tokenizer(BPE())

# Train your model
trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
tokenizer.train(files=["the-verdict.txt"], trainer=trainer)

# Encode your text
output = tokenizer.encode("Hello, y'all! How are you?")
print(output.tokens)
print("Token IDs:", output.ids)

output = tokenizer.encode("supercalifragilisticexpialidocious")
print(output.tokens)
print("Token IDs:", output.ids)


'''
[00:00:00] Pre-processing files (0 Mo)     100%
[00:00:00] Tokenize words                  84       /       84
[00:00:00] Count pairs                     84       /       84
[00:00:00] Compute merges                  6599     /     6599

Example 1:

['H', 'ell', 'o', ', ', 'y', "'", 'all', '! ', 'H', 'ow', ' a', 're ', 'you', '?']
Token IDs: [26, 209, 56, 76, 66, 10, 252, 240, 26, 104, 98, 618, 158, 18]

Example 2:
['sup', 'er', 'c', 'al', 'if', 'ra', 'g', 'i', 'li', 'st', 'ic', 'ex', 'p', 'ial', 'id', 'oc', 'ious']
Token IDs: [2026, 78, 44, 114, 329, 139, 48, 50, 137, 93, 112, 231, 57, 1895, 142, 452, 1904]
'''

# You can work with pretrained models as well

gpt2_tokenizer = Tokenizer.from_pretrained("gpt2")
output = gpt2_tokenizer.encode("Hello, y'all! How are you doing?")
print(output.tokens)
print("Token IDs:", output.ids)

'''
Output: ['Hello', ',', 'Ġy', "'", 'all', '!', 'ĠHow', 'Ġare', 'Ġyou', '?']
Token IDs: [15496, 11, 331, 6, 439, 0, 1374, 389, 345, 1804, 30]

Observe how the words are not broken into subwords in this example.
GPT-2 only breaks words into subwords when necessary — that is, when the full word isn’t in its vocabulary.
GPT-2’s vocab is huge — 50,257 tokens — and includes many full words like:
"doing","you","How","Hello"

So if a word or phrase exists in the vocabulary, it’s not broken down.


Note:
The character Ġ represents a space before a token in GPT-2’s vocabulary:
GPT-2 doesn't treat whitespace as separate characters.
So instead of " y" → it becomes "Ġy", meaning “space followed by y”.
'''

output = gpt2_tokenizer.encode("supercalifragilisticexpialidocious")
print(output.tokens)
print("Token IDs:", output.ids)

'''
Output tokens: ['super', 'cal', 'if', 'rag', 'il', 'ist', 'ice', 'xp', 'ial', 'id', 'ocious']
Token IDs: [16668, 9948, 361, 22562, 346, 396, 501, 42372, 498, 312, 32346]

GPT-2 uses subword tokenization, but only when the full token is not already in its vocab.
The model was trained this way for efficiency and to handle rare/novel words without a full dictionary.
'''