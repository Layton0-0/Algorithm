package Programmers.제일작은수제거하기;

import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        if (arr.length < 2) {
            int[] ans = { -1 };
            return ans;
        }

        int temp = Arrays.stream(arr).min().getAsInt();
        return Arrays.stream(arr).filter(x -> x != temp).toArray();
    }
}
