package sorting;

public class QuickSort {
	
	public static void quickSort(int[] arr, int start, int end) {
		if(start >= end) return;
		int pivot = start;
		int left = start + 1;
		int right = end;
		while(left <= right) {
			// 피벗보다 큰 데이터 찾기(앞에서부터)
			while(left <= end && arr[left] <= arr[pivot])
				left++;
			// 피벗보다 작은 데이터 찾기(뒤에서부터)
			while(right > start && arr[right] >= arr[pivot])
				right--;
			if(left > right) {
				int temp = arr[pivot];
				arr[pivot] = arr[right];
				arr[right] = temp;				
			} else {
				int temp = arr[left];
				arr[left] = arr[right];
				arr[right] = temp;
			}
		}
		// right값과 pivot 값을 바꿨기 때문에 right 위치 전달
		quickSort(arr, start, right - 1);
		quickSort(arr, right + 1, end);
	}

	public static void main(String[] args) {
		int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
		
		quickSort(arr, 0, arr.length-1);
		
		for(int i = 0; i< arr.length; i++) {
			System.out.print(arr[i] + " ");
		}

	}

}
