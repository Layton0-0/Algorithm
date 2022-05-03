package switchTwo;

import java.util.*;

public class Answer {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// n, k의 값 받기
		int n = sc.nextInt();
		int k = sc.nextInt();
		// 배열 a의 모든 원소 받기
		Integer[] a = new Integer[n];
		for(int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}
		// 배열 b의 모든 원소 받기
		Integer[] b = new Integer[n];
		for(int i = 0; i < n; i++) {
			b[i] = sc.nextInt();
		}
		
		// a는 오름차순
		Arrays.sort(a);
		// b는 내림차순으로 정렬
		Arrays.sort(b, Collections.reverseOrder());
		
		// 최대 k번 수행
		for(int i = 0; i < k; i++) {
			// 이미 정렬된 상태니까 각 인덱스 값끼리 비교, a원소가 b보다 작으면 교환
			if(a[i] < b[i]) {
				int temp = a[i];
				a[i] = b[i];
				b[i] = temp;
			}
			// a의 원소가 b의 원소보다 크거나 같으면 반복문을 탈출해 불필요한 연산을 없앤다.
			else break;
		}
		
		// 배열a의 모든 원소의 합을 출력
		long result = 0;
		for(int i = 0; i < n; i++) {
			result += a[i];
		}
		System.out.println(result);
		
		
		
		sc.close();
	}
}
