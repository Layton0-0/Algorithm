import java.util.*;

public class wordSort1181 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Set<String> words = new HashSet<>();
        for(int i = 0; i < n; i++){
            words.add(sc.next());
        }
        ArrayList<String> wordsList = new ArrayList<String>(words);
        Collections.sort(wordsList, new Comparator<String>(){
            @Override
            public int compare(String s1, String s2) {
                if(s1.length() < s2.length()) return -1;
                else if(s1.length() > s2.length()) return 1;
                else return s1.compareTo(s2);
            }
        });

        
        for(String word : wordsList){
            System.out.println(word);
        }
        
        
        

        sc.close();
    }
}
