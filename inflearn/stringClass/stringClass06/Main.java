package inflearn.stringClass.stringClass06;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(solution(str));
        sc.close();
    }

    static String solution(String str) {
        str = str.toLowerCase().replaceAll("[^a-z]", "");
        String str2 = new StringBuilder(str).reverse().toString();
        if (str.equals(str2)) {
            return "YES";
        } else {
            return "NO";
        }
    }
}
