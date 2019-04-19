
# 93. Restore IP Addresses

# https://leetcode.com/problems/restore-ip-addresses/
# https://leetcode.com/problems/restore-ip-addresses/discuss/30972/WHO-CAN-BEAT-THIS-CODE


class Solution(object):
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Backtracking
        def backtracking(s, ip):
            print(s, ip)
            result = []
            if ip.count('.') == 3 and not s:
                return [ip]
            if not s or ip.count('.') > 3:
                return []
            times = min(len(s), 3)
            for i in range(1, times + 1):
                num_s = s[:i]
                if num_s.startswith('0') and len(num_s) > 1:
                    continue
                num = int(num_s)
                if num > 255:
                    continue
                new_ip = ip + '.' + num_s if ip else num_s
                result.extend(backtracking(s[i:], new_ip))
            return result
        return backtracking(s, '')


        # Another method
        result = []
        for a in range(1, 4): # 1 ~ 3
            for b in range(1, 4): # 1 ~ 3
                for c in range(1, 4): # 1 ~ 3
                    for d in range(1, 4): # 1 ~ 3
                        if a + b + c + d != len(s):
                            continue
                        num_a = int(s[:a])
                        num_b = int(s[a:a+b])
                        num_c = int(s[a+b:a+b+c])
                        num_d = int(s[a+b+c:a+b+c+d])
                        in_range = num_a <= 255 and num_b <= 255 and num_c <= 255 and num_d <= 255
                        ip = str(num_a) + '.' + str(num_b) + '.' + str(num_c) + '.' + str(num_d)
                        no_multi_zero = len(ip) == len(s) + 3
                        if in_range and no_multi_zero:
                            result.append(ip)
        return result
