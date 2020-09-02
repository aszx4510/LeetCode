
# 157. Read N Characters Given Read4

# https://leetcode.com/problems/read-n-characters-given-read4/
# https://leetcode.com/problems/read-n-characters-given-read4/discuss/49520/Python-solution-with-explainations-and-comments


"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0
        while n > 0:
            # Read file to buffer
            buffer = [''] * 4
            len_buf = read4(buffer)
            
            # If no more char in file, return idx
            if not len_buf:
                return idx
            
            # Write buffer in "buf"
            for i in range(min(len_buf, n)):
                buf[idx] = buffer[i]
                idx += 1
                n -= 1
        return idx
