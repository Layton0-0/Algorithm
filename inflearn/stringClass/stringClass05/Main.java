// 특정 문자 뒤집기(toCharArray())
package inflearn.stringClass.stringClass05;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] str = sc.next().toCharArray();

        System.out.println(solution(str));

        sc.close();
    }

    static String solution(char[] str) {
        String answer = "";

        int lt = 0, rt = str.length - 1;
        while (lt < rt) {
            if (!Character.isAlphabetic(str[lt])) {
                lt++;
            } else if (!Character.isAlphabetic(str[rt])) {
                rt--;
            } else {
                char temp = str[lt];
                str[lt] = str[rt];
                str[rt] = temp;
                lt++;
                rt--;
            }
        }
        answer = String.valueOf(str);

        return answer;

    }

}
