package 기출문제.티맥스;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class First {
	public static void main(String[] args) {
		String[] votes = {"AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"};
		int k = 2;
		System.out.println(solution(votes, k));
	}
	public static String solution(String[] votes, int k) {
		String answer = "";
		Map<String, Integer> voteMap = new HashMap<>();
		for(int i = 0; i < votes.length; i++) {
			if(!voteMap.containsKey(votes[i])) {
				voteMap.put(votes[i], 1);	
			} else {
				voteMap.replace(votes[i], voteMap.get(votes[i])+1);
			}
		}
		List<Map.Entry<String, Integer>> entryList = new LinkedList<>(voteMap.entrySet());
		
		entryList.sort(new Comparator<Map.Entry<String, Integer>>() {

			@Override
			public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
				if(o1.getValue() == o2.getValue()) {
					return -(o1.getKey().compareTo(o2.getKey()));
					
				} else {
					return o1.getValue()- o2.getValue();
				}
			}
			
		});
		int sum = 0;
		for(Map.Entry<String, Integer> entry: entryList) {
			System.out.println("key: "+ entry.getKey() + " value: " + entry.getValue());
			
		}	
		for(int i = 0; i < k; i++) {
			sum += entryList.get(entryList.size()-i-1).getValue();
		}
		int count = 0;
		for(int i = 0; i < sum; i++) {

			count += entryList.get(i).getValue();
			System.out.println(count);

			
			if(sum <= count) {
				answer = entryList.get(i-1).getKey();
				System.out.println("답: " +answer);
				break;
			}
		}
		
		
		//System.out.println(answer);
		return answer;
	}
}

class Car {
	private String carName;
	private int carVoteCount;
	
	public Car(String carName) {
		super();
		this.carName = carName;
		this.carVoteCount = 0;
	}

	public String getCarName() {
		return carName;
	}

	public void setCarName(String carName) {
		this.carName = carName;
	}

	public int getCarVoteCount() {
		return carVoteCount;
	}

	public void setCarVoteCount(int carVoteCount) {
		this.carVoteCount = carVoteCount;
	}
	
	
	
	
}
