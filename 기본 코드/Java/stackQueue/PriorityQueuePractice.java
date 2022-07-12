package Java.stackQueue;

import java.util.PriorityQueue;

public class PriorityQueuePractice {

	public static void main(String[] args) {
		PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
		priorityQueue.add(5);
		priorityQueue.add(1);
		priorityQueue.add(2);
		
		priorityQueue.poll();
		while(!priorityQueue.isEmpty()) {
			System.out.println(priorityQueue.poll());
		}
	}

}
