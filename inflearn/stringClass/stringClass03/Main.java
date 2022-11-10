package inflearn.stringClass.stringClass03;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(solution(str));
        sc.close();
    }

    static String solution(String str) {
        String answer = "";
        String[] strArr = str.split(" ");
        for (String s : strArr) {
            if (s.length() > answer.length()) {
                answer = s;
            }
        }
        return answer;
    }
}