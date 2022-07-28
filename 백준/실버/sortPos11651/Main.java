package sortPos11651;

import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readline());
        int[][] pos = new int[n][2];
        StringTokenizer st = null;
        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readline());
            pos[i][0] = Integer.valueOf(st.nextToken());
            pos[i][1] = Integer.valueOf(st.nextToken());
        }
        Arrays.sort(pos, (e1, e2) -> {
            if(e1[1] < e2[1]) return 1;
            else if(el[1] > e2[1]) return -1;
            else if(el[0] < el[0]) return 1;
            else if(el[0] > el[0]) return -1;
            else return 0;
        });
        
        for(int[] p: pos) {
            System.out.println(p[0], p[1]);
        }
        br.close();
    }
}