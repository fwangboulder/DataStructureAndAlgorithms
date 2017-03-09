"""
68. Text Justification   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 48273
Total Submissions: 265143
Difficulty: Hard
Contributors: Admin
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Hide Company Tags LinkedIn Airbnb Facebook
Hide Tags String

"""
"""
note:
step 1: distribute
store (total lengh, number of words) for convenience in the second step

step 2: add spaces
#note if total length==1, add spaces to the end
# if it is the last line, add spaces to the end
# else: calculate the average number of spaces
  The mod!=0 means start from the second word (important), an extra spact should be add in front first until mod==0
  space=numberOfSpaces*' '
  space.join(array[1:])

"""


class Solution(object):

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return [' ' * maxWidth]
        res = []
        s = map(len, words)

        # distribute the world
        for i in xrange(1, len(s)):
            s[i] += s[i - 1]
        i = 0
        base = 0
        start = 0
        # consider one word condition
        if len(words) == 1:
            return [words[0] + (maxWidth - s[0]) * ' ']
        #1+ words in array
        while i < len(s) and s[i] - base + (i - start) <= maxWidth:
            i += 1
            if i < len(s) and s[i] - base + (i - start) > maxWidth:
                l = s[i - 1] - base
                # store the words when reaching the limit of maxWidth in
                # res,the first element is a tuple recording the total
                # #characters and number of words
                res.append([(l, i - start)] + words[start:i])
                base = s[i - 1]
                start = i
            elif i >= len(s):
                l = s[i - 1] - base
                # when the counting reach the end of the array, stored
                res.append([(l, i - start)] + words[start:i])
        # above for distribute the words
        # below for adding spaces
        print res
        for i, v in enumerate(res):
            # add space to the end if it is the last line
            if i == len(
                    res) - 1 and v[0][1] != 1 and maxWidth - v[0][0] - v[0][1] + 1 > 0:
                endSpace = ' ' * (maxWidth - v[0][0] - v[0][1] + 1)
                res[i] = ' '.join(v[1:]) + endSpace

            # if only contains one words, add space in the end
            elif i < len(res) and v[0][1] == 1 and v[0][0] <= maxWidth:
                endSpace = ' ' * (maxWidth - v[0][0])
                res[i] = ''.join(v[1:]) + endSpace
            # spaces are distributed evenly
            else:
                space = ' ' * ((maxWidth - v[0][0]) / (v[0][1] - 1))
                mod = (maxWidth - v[0][0]) % (v[0][1] - 1)
                for j in range(2, len(v)):
                    if mod:
                        v[j] = ' ' + v[j]
                        mod -= 1
                    else:
                        break

                res[i] = space.join(v[1:])
        return res
