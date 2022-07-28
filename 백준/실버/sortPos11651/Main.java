package 백준.실버.sortPos11651;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[][] pos = new int[n][2];
        StringTokenizer st = null;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            pos[i][0] = Integer.valueOf(st.nextToken());
            pos[i][1] = Integer.valueOf(st.nextToken());
        }

        Arrays.sort(pos, (e1, e2) -> {
            if (e1[1] == e2[1])
                return e1[0] - e2[0];
            return e1[1] - e2[1];
        });

        for (int[] p : pos) {
            System.out.println(p[0] + " " + p[1]);
        }
        br.close();
    }
}