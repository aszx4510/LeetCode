
# 468. Validate IP Address

# https://leetcode.com/problems/validate-ip-address/
# https://leetcode.com/problems/validate-ip-address/discuss/95484/PythonJava-Easy-Understand-Solution


class Solution:
    def validIPAddress(self, IP: str) -> str:
        def is_ipv4(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        def is_ipv6(s):
            if len(s) > 4:
                return False
            try:
                return int(s, 16) >= 0 and s[0] != '-'
            except:
                return False

        if IP.count('.') == 3 and all(is_ipv4(s) for s in IP.split('.')):
            return 'IPv4'
        if IP.count(':') == 7 and all(is_ipv6(s) for s in IP.split(':')):
            return 'IPv6'
        return 'Neither'
