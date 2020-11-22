def is_sub_array(s, S):
    litl_ind = 0

    for big_ind in range(len(S)):
        if S[big_ind] == s[litl_ind]:
            litl_ind += 1
            if litl_ind == len(s):
                return True

            # If commented s from script is subarray of S, our code should have next:, compl = O(n+m)
            # while s[litl_ind] == s[litl_ind - 1]:
            #     litl_ind += 1
            #     if litl_ind == len(s):
            #         return True
    return False


if __name__ == '__main__':
    S = ['A', 'B', 'C', 'B', 'B', 'D']
    s = ['B', 'C', 'B', 'D']
    #s = ['A', 'A', 'A', 'A', 'B', 'C']  # - ???
    print(is_sub_array(s, S))
