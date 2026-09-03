trie={}

q=int(input())

for _ in range(q):

    operation,word=input().split()

    if operation=="INSERT":
        node=trie

        for ch in word:
            if ch not in node:
                node[ch]={}
            node=node[ch]

        node["$"]=True

    elif operation=="SEARCH":
        node=trie
        found=True

        for ch in word:
            if ch not in node:
                found=False
                break
            node=node[ch]

        if "$" not in node:
            found=False

        print("YES" if found else "NO")

    elif operation=="PREFIX":
        node=trie
        found=True

        for ch in word:
            if ch not in node:
                found=False
                break
            node=node[ch]

        print("YES" if found else "NO")