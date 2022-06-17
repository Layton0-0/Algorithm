package stackQueue;

import java.util.Collections;
import java.util.PriorityQueue;

public class PriorityQueuePractice {

	public static void main(String[] args) {
		PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
		PriorityQueue<Integer> rPriorityQueue = new PriorityQueue<>(Collections.reverseOrder());
		priorityQueue.add(5);
		priorityQueue.add(1);
		priorityQueue.add(2);
		
		priorityQueue.poll();
		while(!priorityQueue.isEmpty()) {
			System.out.println(priorityQueue.poll());
		}
	}

}
