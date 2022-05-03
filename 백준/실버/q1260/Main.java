package q1260;

import java.util.*;

public class Main {
	public static int n, m, v;
	public static boolean[] visitedDfs = new boolean[1001];
	public static boolean[] visitedBfs = new boolean[1001];
	public static ArrayList<ArrayList<Integer>> nodeInfo = new ArrayList<ArrayList<Integer>>();
	
	public static void dfs(int start) {
		visitedDfs[start] = true;
		
		System.out.print(start + " ");
		
		for(int i = 0; i < nodeInfo.get(start).size(); i++) {
			int y = nodeInfo.get(start).get(i);
			if(!visitedDfs[y])
				dfs(y);
		}
	}
	
	public static void bfs(int start) {
		Queue<Integer> q = new LinkedList<Integer>();
		visitedBfs[start] = true;
		
		q.offer(start);
				
		while(!q.isEmpty()) {
			int now = q.poll();
			System.out.print(now + " ");
			for(int i = 0; i < nodeInfo.get(now).size(); i++) {
				int y = nodeInfo.get(now).get(i);
				if(!visitedBfs[y]) {
					visitedBfs[y] = true;
					q.offer(y);				
				}
			}
		}
	}

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		v = sc.nextInt();
		
		// 총 n까지 노드가 있기 때문에 n까지 만들어 줌. 초기화.
		for(int i = 0; i < n + 1; i++) {
			nodeInfo.add(new ArrayList<Integer>());
		}

		// 각 노드를 입력받음과 동시에 저장. 양 쪽에 동시에 저장.
		for(int i = 0; i < m; i++) {
			int node1 = sc.nextInt();
			int node2 = sc.nextInt();
			nodeInfo.get(node1).add(node2);	
			nodeInfo.get(node2).add(node1);
		}
		
		// 작은 수부터 탐색하기 위해 정렬
		for(int i = 0; i < n + 1; i++) {
			Collections.sort(nodeInfo.get(i));			
		}
				
		dfs(v);
		System.out.println();
		bfs(v);
		
		
		sc.close();
	}

}
