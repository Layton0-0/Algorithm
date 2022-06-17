package dynamicPrograming;

public class FiboBottomUp {
	
	public static long[] d = new long[100];
	
	public static void main(String[] args) {
		// 첫 번째, 두 번째 피보나치 수의 값은 1
		d[1] = 1;
		d[2] = 1;
		int n = 50; // 50번째 피보나치 수를 계산
		
		// 반복문을 통해 보텀업 다이나믹 프로그래밍 구현
		for(int i = 3; i <= n; i++) {
			d[i] = d[i-1]+d[i-2];
		}
		System.out.println(d[n]);
	}
}
