import java.util.Scanner;
import java.util.ArrayList;
class Modulo{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        ArrayList<Integer> nums = new ArrayList<>();
        for(int i = 0; i < 10; i++){
            int n = s.nextInt();
            if(!nums.contains(n % 42))nums.add(n % 42);
        }
        System.out.println(nums.size());
        s.close();
    }
}
