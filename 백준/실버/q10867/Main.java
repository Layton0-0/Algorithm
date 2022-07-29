package 백준.실버.q10867;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        Set<Integer> s = new TreeSet<>();
        while (st.hasMoreTokens()) {
            s.add(Integer.valueOf(st.nextToken()));

        }
        for (int i : s) {
            System.out.print(i + " ");
        }
    }
}
