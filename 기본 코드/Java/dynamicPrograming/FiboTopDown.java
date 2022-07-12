package Java.dynamicPrograming;

public class FiboTopDown {

	// 한 번 계산된 결과를 메모이제이션 하기 위함 -> 배열 초기화
	public static long[] d = new long[100];
	// 재귀 함수로 탑다운 다이나믹 프로그래밍 구현
	public static long fibo(int x) {
		// 재귀 종료 조건
		if(x == 1 || x == 2) {
			return 1;
		}
		// 이미 계산한 적 있는 문제라면 연산 수행 없이 그대로 값 반환
		if(d[x] != 0) {
			return d[x];
		}
		// 계산하지 않은 문제는 점화식에 따라 값 반환
		d[x] = fibo(x - 1) + fibo(x - 2);
		return d[x];
	}
	
	public static void main(String[] args) {
		System.out.println(fibo(50));

	}

}
