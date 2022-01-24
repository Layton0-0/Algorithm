package exitMaze;

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
	public static int[][] maze = new int[200][200];
	
	// 이동할 4가지 방향 정의 (상하좌우)
	public static int dx[] = {-1, 1, 0, 0};
	public static int dy[] = {0, 0, -1, 1};
	
	public static int bfs(int x, int y) {
		Queue<Node> q = new LinkedList<>();  
		q.offer(new Node(x, y));
		
		// 큐가 빌 때까지 반복하기
		while(!q.isEmpty()) {
			Node node = q.poll();
			x = node.getX();
			y = node.getY();
			
			// 현재 위치에서 4가지 방향으로의 위치 확인
			for(int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				// 미로 찾기 공간을 벗어난 경우 무시
				if(nx < 0 || nx >= n || ny < 0 || ny >= m)
					continue;
				if(maze[nx][ny] == 1) {
					maze[nx][ny] = maze[x][y] + 1;
					q.offer(new Node(nx, ny));
				}
			}
		}
		return maze[n - 1][m - 1];
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// n과 m 입력받기
		n = sc.nextInt();
		m = sc.nextInt();
		sc.nextLine();
		// 미로 정보 입력받기
		for(int i = 0; i < n; i++) {
			String str = sc.nextLine();
			for(int j = 0; j < m; j++) {
				maze[i][j] = str.charAt(j) - '0';
			}
		}		
		
		// bfs를 수행한 결과 출력
		System.out.println(bfs(0, 0));
		
		
		
		sc.close();
	}

}
