import java.util.Scanner;
class Death_Knight_Hero{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int count = 0;
        for(int i = 0; i < n; i++){
            String b = s.next();
            if(!b.contains("CD"))count++;
        }
        System.out.println(count);
    }
}
