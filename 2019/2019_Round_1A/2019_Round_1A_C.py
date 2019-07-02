# Python 3.7.3
import collections

class TreeNode():
    def __init__(self):
        self.suffix = ""
        self.word_count = 0
        self.words = []
        self.children = []


def main():
    T = int(input())

    for test_case in range(T):
        N = int(input())
        words = []
        for _ in range(N):
            words.append(input().strip())
        # Construct suffix tree first
        root = TreeNode()
        root.words = words
        root.word_count = len(words)
        q = collections.deque([root])
        while q:
            curr = q.popleft()
            if curr.suffix != "" and len(curr.words) <= 2:
                continue
            next_suffix_len = len(curr.suffix) + 1
            suffix_map = {}
            for word in curr.words:
                suffix = word[-next_suffix_len:]
                if suffix in suffix_map:
                    suffix_map[suffix].append(word)
                else:
                    suffix_map[suffix] = [word]
            for suffix in suffix_map:
                new_node = TreeNode()
                new_node.suffix = suffix
                new_node.word_count = len(suffix_map[suffix])
                new_node.words = suffix_map[suffix]
                curr.children.append(new_node)
                curr.word_count -= new_node.word_count
                q.append(new_node)
        # Now from leaf, find pairs!
        def dfs(node):
            valid_set_count = 0
            # Visit child node first
            for child in node.children:
                valid_set_count += dfs(child)
            # Now visit current node
            if node.suffix != "":
                # Get total word count
                child_count = 0
                for child in node.children:
                    child_count += child.word_count
                node.word_count += child_count
                if node.word_count >= 2:
                    node.word_count -= 2
                    valid_set_count += 2
            return valid_set_count
        print("Case #{}: {}".format(test_case + 1, dfs(root)))


main()