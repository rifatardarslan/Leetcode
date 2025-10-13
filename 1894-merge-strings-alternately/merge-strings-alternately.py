class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list3 = []
        list1 = list(word1)
        list2 = list(word2)

        min_len = min(len(list1), len(list2))

        for i in range(min_len):
            list3.append(list1[i])
            list3.append(list2[i])

        if len(word1) > len(word2):
            list3.extend(list1[min_len:])
        elif len(word2) > len(word1):
            list3.extend(list2[min_len:])

        return "".join(list3)
