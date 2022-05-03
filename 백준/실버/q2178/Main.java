package q2178;

import java.util.*;

class Node {
	private int x;
	private int y;
	public Node(int x, int y) {
		this.x = x;
		this.y = y;
	}	
	public int getX() {
		return this.x;
	}	
	public int getY() {
		return this.y;
	}	
}

public class Main {
	public static int n, m;
	public static int[][] maze = new int[100][100];
	
	// 상하좌우 순서
	public static int[] moveX = {-1, 1, 0, 0};
	public static int[] moveY = {0, 0, -1, 1};

	public static int bfs() {
		// bfs로 문제를 풀기 위해 큐 생성
		// 시작지점에서 가장 가까운 노드부터 차례로 모든 노드를 탐색하기 때문에 bfs 사용.
		Queue<Node> route = new LinkedList<>();
		route.add(new Node(0, 0));
		
		while(!route.isEmpty()) {
			Node now = route.poll();
			int x = now.getX();
			int y = now.getY();
			for(int i = 0; i < 4; i++) {
				int nx = x + moveX[i];
				int ny = y + moveY[i];
				if(nx <= -1 || nx >= n || ny <= -1 || ny >= m) {
					continue;
				}
				if(maze[nx][ny] == 1) {
					maze[nx][ny] = maze[x][y] + 1;
					route.offer(new Node(nx, ny));
				}
				
			}
		}		
		return maze[n-1][m-1];			
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		sc.nextLine();
		
		for(int i = 0; i < n; i++) {
			String str = sc.nextLine();
			for(int j = 0; j < m; j++) {
				maze[i][j] = str.charAt(j) - '0';
			}
		}
		
		System.out.println(bfs());
		
		
		sc.close();
	}

}
