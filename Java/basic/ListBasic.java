package Java.basic;

import java.util.*;

public class ListBasic {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        List<String> list2 = new ArrayList<>();

        list.add("엄마");
        list.add(1, "아빠");
        list2.add("마마");
        for (String temp : list) {
            System.out.print(temp + " ");
        }
        System.out.println();
        list2.addAll(list);
        for (String temp : list2) {
            System.out.print(temp + " ");
        }

        list.get(0);
        list.set(0, "윤정");

        list.indexOf("윤정");
        list.lastIndexOf("아빠");

        list.remove(0);
        System.out.println();
        for (String temp : list) {
            System.out.print(temp + " ");
        }

        // list에서 list2에 들어있는 모든 값 삭제
        list.removeAll(list2);
        // list에서 list2에 있는 값빼고 전부 삭제
        list.retainAll(list2);
        // 전부 삭제
        list.clear();

        // 길이가 0이면 참
        list.isEmpty();
        // 길이
        list.size();

        list.contains("서울");
        list.containsAll(list2);

        // list.removeIf(k -> k % 2 != 0);

        String[] temp = { "dsfsd", "eafdsi", "sdfiwefhj" };
        List<String> sList = new ArrayList<>(Arrays.asList(temp));
        System.out.println(sList.get(0));

        List<Integer> iList = new ArrayList<>(Arrays.asList(3, 45, 43, 55, 2));
        int[] is = new int[iList.size()];
        list.toArray(temp);
        is = iList.stream().mapToInt(i -> i).toArray();

    }
}
