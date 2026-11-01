import heapq

def huffman_encoding(chars, freq):
    heap = [[freq[i], chars[i]] for i in range(len(chars))]
    heapq.heapify(heap)

    codes = {}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for char in left[1]:
            codes[char] = codes.get(char, "") + "0"

        for char in right[1]:
            codes[char] = codes.get(char, "") + "1"

        new_node = [left[0] + right[0], left[1] + right[1]]
        heapq.heappush(heap, new_node)

    return codes

n = int(input("Enter number of characters: "))

chars = []
freq = []

for i in range(n):
    ch = input("Enter character: ")
    f = int(input("Enter frequency: "))
    chars.append(ch)
    freq.append(f)

codes = huffman_encoding(chars, freq)

print("\nHuffman Codes:")
for ch in chars:
    print(ch, ":", codes[ch])