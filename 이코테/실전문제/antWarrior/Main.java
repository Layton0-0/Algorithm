package antWarrior;

import java.util.*;

public class Main {
	public static int[] dp = new int[100];
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] meal = new int[n + 1];
		for(int i = 1; i <= n; i++) {
			meal[i] = sc.nextInt();
		}
		dp[1] = meal[1]; 
		dp[2] = Math.max(meal[1], meal[2]);
		for(int i = 3; i <= n; i++) {
			dp[i] = Math.max(dp[i - 1], dp[i - 2] + meal[i]);
		}
		
		System.out.println(dp[n]);
		
		
		sc.close();
	}
}
