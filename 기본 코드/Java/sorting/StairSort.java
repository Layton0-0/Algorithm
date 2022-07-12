package Java.sorting;

public class StairSort {
	// 배열해야하는 값 중 가장 큰 값
	public static final int MAX_VALUE = 9;
	
	public static void main(String[] args) {
		// 모든 원소의 값이 0보다 크거나 같다고 가정
		int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
		// 모든 범위를 포함하는 배열 선언(모든 값은 0으로 초기화)
		// 크기가 9인 배열을 만들면 가장 큰 인덱스가 8이게 됨. 그래서 1을 더해줌.
		int[] cnt = new int[MAX_VALUE + 1];
		
		for(int i = 0; i < arr.length; i++) {
			cnt[arr[i]] += 1; // 각 데이터에 해당하는 인덱스 값의 증가
		}
		
		for(int i = 0; i <= MAX_VALUE; i++) { // 새로운 배열의 끝까지 출력
			for(int j = 0; j < cnt[i]; j++) { // 인덱스를 센 횟수만큼 출력
				System.out.print(i + " "); // 띄어쓰기를 기준으로 등장한 횟수만큼 인덱스 출력
			}
		}
	}

}
