package Java.basic;

public class StringBasic {
    public static void main(String[] args) {
        String str = "abcdefu cKyou";
        System.out.println("str.length() -> " + str.length());
        System.out.println("str.isEmpty() -> " + str.isEmpty());

        System.out.println(str.charAt(3));
        System.out.println(str.indexOf("f"));
        System.out.println(str.lastIndexOf("f"));

        // System.out.println(str.substring(2, -1));
        System.out.println(str.substring(2, 4));
        System.out.println(str.substring(3));

        System.out.println(str.replace("u", "k"));

        System.out.println(str.equals("abc"));
        System.out.println(str.equals("abcdefu"));
        System.out.println(str.contains("de"));

        // 띄어쓰기도 하나하나 잘라서 저장
        System.out.println(str.split(" ")[1]);
        // 띄어쓰기 다 없애고 문자열만 저장
        // System.out.println(str.split());

        // 앞 뒤 공백 제거, 문자열 사이 공백 제거 아님
        System.out.println(str.trim());

        System.out.println(str.toLowerCase());
        System.out.println(str.toUpperCase());

        System.out.println(str);

        // 사전 순으로 반환. 오름차순
        System.out.println(str.compareTo("abc"));
        System.out.println(str.compareTo("abcdefu ckyou"));
        System.out.println(str.compareToIgnoreCase("abcdefu ckyou"));

        System.out.println(Integer.valueOf("500"));
        System.out.println(Integer.toString(500));
    }
}
