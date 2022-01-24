package drinkIceWater;

import java.util.*;

public class Mine {

	public static int[][] box = new int[1000][1000];
	public static int n, m;
	
	public static boolean dfs(int x, int y) {
		if(x <= -1 || y <= -1 || x >= n || y >= m) {
			return false;
		}
		
		if(box[x][y] == 0) {
			box[x][y] = 1;
			dfs(x - 1, y);
			dfs(x + 1, y);
			dfs(x, y + 1);
			dfs(x, y - 1);
			return true;
		}
		
		return false;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		m = sc.nextInt();
		
		sc.nextLine();

		for (int i = 0; i < n; i++) {
			String str = sc.nextLine();
			for (int j = 0; j < m; j++) {
				box[i][j] = str.charAt(j) - '0';
			}
		}
		sc.close();
		
		int count = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(dfs(i, j)) {
					count++;
				}
			}
		}

		System.out.println(count);
		

	}

}
