package Programmers.핸드폰번호가리기;

public class Main {
    class Solution {
        public String solution(String phone_number) {
            String answer = "";
            int l = phone_number.length();
            for (int i = 0; i < l - 4; i++) {
                answer += "*";
            }
            answer += phone_number.substring(l - 4);
            return answer;
        }
    }
}
