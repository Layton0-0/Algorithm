package Java.stackQueue;

import java.util.*;

public class QueuePractice {
  public static void main(String[] args) {
    Queue<Integer> q = new LinkedList<>();
    q.offer(5);
    q.offer(9);
    q.offer(4);
    q.poll();

    while(!q.isEmpty()){
      System.out.println(q.poll() + " ");
    }
  }
}
