package Java.dfsBfs;

public class DfsBfs {

	public static void main(String[] args) {
		final int INF = 999999999; 
		
		int[][] graph = {
				{0, 7, 5},
				{7, 0, INF},
				{5, INF, 0}
		};
		
		for(int[] e: graph) {
			for(int f: e)
				System.out.print(f + " ");
			System.out.println();
		}

	}

}
