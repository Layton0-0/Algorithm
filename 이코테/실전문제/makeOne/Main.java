package makeOne;

import java.util.*;

public class Main {
	public static int[] dpTable = new int[30000];
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		
		for(int i = 2; i <= x; i++){
			// 바로 전 숫자보다 연산 횟수가 1 많다는 디폴트로 1을 뺐을 때의 연산 횟수를 기본으로 정함.
			dpTable[i] = dpTable[i-1] + 1;
			if(dpTable[i] % 2 == 0) {
				// 2로 나눴을 때와 1을 뺀 연산 횟수를 비교해 작은 값으로 최적해 찾음.
				// i / 2 때의 값에 1을 더해야 i때의 연산 횟수를 구할 수 있음. 
				dpTable[i] = Math.min(dpTable[i], dpTable[i / 2] + 1);
			}
			if(dpTable[i] % 3 == 0) {
				dpTable[i] = Math.min(dpTable[i], dpTable[i / 3] + 1);
			}
			if(dpTable[i] % 5 == 0) {
				dpTable[i] = Math.min(dpTable[i], dpTable[i / 5] + 1);
			}
		}
		
		System.out.println(dpTable[x]);
		
		sc.close();
	}

}
