// 단어 뒤집기(StringBuilder 이용법 또는 직접 뒤집기)
package inflearn.stringClass.stringClass04;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] strs = new String[n];

        for (int i = 0; i < n; i++) {
            strs[i] = sc.next();
        }

        for (String s : solution(n, strs)) {
            System.out.println(s);
        }

        sc.close();
    }

    static ArrayList<String> solution(int n, String[] strs) {
        ArrayList<String> answers = new ArrayList<>();
        for (String s : strs) {
            String answer = new StringBuilder(s).reverse().toString();
            answers.add(answer);
        }

        return answers;

    }

}