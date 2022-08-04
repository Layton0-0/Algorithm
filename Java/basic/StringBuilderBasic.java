package Java.basic;

public class StringBuilderBasic {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();

        sb.append("abc");
        System.out.println(sb);
        sb.insert(2, "es");
        System.out.println(sb);

        // 2~3까지 삭제
        sb.delete(2, 4);
        System.out.println(sb);
        // 해당 인덱스의 문자 삭제
        sb.deleteCharAt(1);
        System.out.println(sb);

        sb.setCharAt(0, 's');
        System.out.println(sb);

        sb.reverse();
        System.out.println(sb);

        sb.append("dfsafasdfsa");
        System.out.println(sb);
        sb.setLength(4);
        System.out.println(sb);
        System.out.println(sb.length());
    }
}
