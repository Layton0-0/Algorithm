package inflearn.stringClass.stringClass07;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(solution(str));
        sc.close();
    }

    static int solution(String str) {
        str = str.replaceAll("[^0-9]", "");
        return Integer.parseInt(str);
    }
}