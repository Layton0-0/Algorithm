package findItem;

import java.util.*;
import java.io.*;

public class Main {
	public static int n, m;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// n 입력받고 부품도 입력받기
		n = Integer.valueOf(br.readLine());
		String[] nNumS = br.readLine().split(" ");
		int[] nNum = new int[n];
		// 정수형으로 저장
		for(int i = 0; i < n; i++) {
			nNum[i] = Integer.valueOf(nNumS[i]);
		}
		
		// m 입력받고 부품도 입력받기
		m = Integer.valueOf(br.readLine());
		String[] mNumS = br.readLine().split(" ");
		int[] mNum = new int[m];
		// 정수형으로 저장
		for(int i = 0; i < m; i++) {
			mNum[i] = Integer.valueOf(mNumS[i]);
		}
		
		findIt(nNum, mNum);
		
		br.close();
	}
	
	public static void findIt(int[] myItem, int[] yourItem) {
		Arrays.sort(myItem);
		
		for(int i = 0; i < m; i++) {
			if(binarySearch(myItem, 0, n - 1, yourItem[i]) > -1)
				System.out.print("yes ");
			else
				System.out.print("no ");
		}
	}
	
	public static int binarySearch(int[] arr, int start, int end, int target) {
		if(start > end)
			return -1;
		int mid = (start + end) / 2;
		if(arr[mid] == target)
			return mid;
		else if(arr[mid] > target)
			return binarySearch(arr, start, mid - 1, target);
		else
			return binarySearch(arr, mid + 1, end, target);
	}
	
	public static int binarySearch2(int[] arr, int start, int end, int target) {
		while(start <= end) {
			int mid = (start + end) / 2;
			if(arr[mid] == target)
				return mid;
			else if(arr[mid] > target)
				end = mid - 1;
			else
				start = mid + 1;
		}
		return -1;
	}
}
