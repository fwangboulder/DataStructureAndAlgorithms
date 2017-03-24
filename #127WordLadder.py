"""
127. Word Ladder Add to List
DescriptionSubmissionsSolutions
Total Accepted: 114661
Total Submissions: 595987
Difficulty: Medium
Contributors: Admin
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

Hide Company Tags Amazon LinkedIn Snapchat Facebook Yelp

"""


class Solution(object):

    def ladderLength(self, begin, end, words_list):
        """
        :type begin: str
        :type end: str
        :type wordList: List[str]
        :rtype: List[List[str]]

        If we know source and destination, we can build the word tree by going forward in one direction and backwards in the other. We stop when we have found that a word in the next level of BFS is in the other level, but first we need to update the tree for the words in the current level.

        Then we build the result by doing a DFS on the tree constructed by the BFS.

        The difference between normal and double BFS is that the search changes from O(k^d) to O(k^(d/2) + k^(d/2)). Same complexity class
        """

        # Solution using double BFS
        def construct_paths(source, dest, tree):
            if source == dest:
                return [[source]]
            return [[source] + path for succ in tree[source]
                    for path in construct_paths(succ, dest, tree)]

        def add_path(tree, word, neigh, is_forw):
            if is_forw:
                tree[word] += neigh,
            else:
                tree[neigh] += word,

        def bfs_level(this_lev, oth_lev, tree, is_forw, words_set):
            if not this_lev:
                return False
            if len(this_lev) > len(oth_lev):
                return bfs_level(
                    oth_lev, this_lev, tree, not is_forw, words_set)
            for word in (this_lev | oth_lev):
                words_set.discard(word)
            next_lev, done = set(), False
            while this_lev:
                word = this_lev.pop()
                for c in string.ascii_lowercase:
                    for index in range(len(word)):
                        neigh = word[:index] + c + word[index + 1:]
                        if neigh in oth_lev:
                            done = True
                            add_path(tree, word, neigh, is_forw)
                        if not done and neigh in words_set:
                            next_lev.add(neigh)
                            add_path(tree, word, neigh, is_forw)
            return done or bfs_level(
                next_lev, oth_lev, tree, is_forw, words_set)
        if end not in words_list:
            return 0
        tree, path, paths = collections.defaultdict(list), [begin], []
        is_found = bfs_level(set([begin]), set(
            [end]), tree, True, set(words_list))
        res = construct_paths(begin, end, tree)
        if not res:
            return 0
        return len(res[0])
