package Programmers.평균구하기;

import java.util.*;

public class Main {
    public double solution(int[] arr) {
        return Arrays.stream(arr).average().orElse(0);
    }
}
