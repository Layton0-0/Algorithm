package printStudent;

import java.util.*;

public class Main{
	public static int n;
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);		
		n = sc.nextInt();
//		sc.nextLine();은 다음에 사용할 메소드가 nextLine일 경우에만 사용. 버퍼를 비워주기 위함.
		ArrayList<Student> student = new ArrayList<>();
		
		for(int i = 0; i < n; i++) {
			// sc.next()는 공백 전의 문자열을 반환해준다.
			// sc.nextLine()은 엔터치기 전까지의 문자열을 반환한다.
			String name = sc.next();
			int score = sc.nextInt();
			student.add(new Student(name, score));
		}
		
		Collections.sort(student);
		
		for(int i = 0; i < n; i++) {
			System.out.print(student.get(i).getStdName() + " ");
		}
		
		sc.close();
	}

}

class Student implements Comparable<Student>{
	private String stdName;
	private int stdScore;
	public Student(String stdName, int stdScore) {
		this.stdName = stdName;
		this.stdScore = stdScore;
	}	
	public String getStdName() {
		return this.stdName;
	}
	public int getStdScore() {
		return this.stdScore;
	}
	
	@Override
	public int compareTo(Student comp) {
		return this.stdScore - comp.stdScore;
	}
}
