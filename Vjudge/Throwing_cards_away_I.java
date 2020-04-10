import java.util.Scanner;
import java.util.ArrayList;
public class Throwing_cards_away_I
{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        ArrayList<Integer> nums = new ArrayList<>();
        while(s.hasNextInt()){
            int n = s.nextInt();
            nums.add(n);
        }
        for(Integer n: nums){
            if(n > 1){
                ArrayList<Integer> a = new ArrayList<>();
                for(int i = 1; i <= n; i++)a.add(i);
                System.out.print("Discarded cards: ");
                while(a.size() > 1){
                    if(a.size() != 2)System.out.print(a.get(0) + ", ");
                    else System.out.print(a.get(0));
                    a.remove(0);
                    int temp = a.get(0);
                    a.remove(0);
                    a.add(temp);
                }
                System.out.println();
                System.out.println("Remaining card: " + a.get(0));
            }
            if(n == 1){
            	System.out.println("Discarded cards:");
            	System.out.println("Remaining card: 1");
            }
        }
        s.close();
    }
}
