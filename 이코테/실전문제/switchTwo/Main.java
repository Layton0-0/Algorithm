package switchTwo;

import java.util.*;

public class Main {

	public static int n, k;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		k = sc.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		int sum = 0;
		
		for(int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}
		for(int i = 0; i < n; i++) {
			b[i] = sc.nextInt();
		}
		
		switchK(a, b);
		
		for(int num: a) {		
			sum += num;
		}
		
		System.out.println(sum);
		
		sc.close();
	}
	
	public static void switchK(int[] a, int[] b) {
		int indexA = 0;
		int indexB = 0;
		for(int j = 0; j < k; j++) {
			for(int i = 0; i < n; i++) {
				if(a[i] <= a[indexA]) {
					indexA = i;
				}
				if(b[i] >= b[indexB]) {
					indexB = i;
				}
			}
			// 둘의 값을 교환
			if(a[indexA] <= b[indexB]) {
				int temp = a[indexA];
				a[indexA] = b[indexB];
				b[indexB] = temp;
			}
		}

	}

}
