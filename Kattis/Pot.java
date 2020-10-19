import java.util.Scanner;
class Pot{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int sum = 0;
        for(int i = 0; i < n; i++){
            int a = s.nextInt();
            int b = a % 10;
            sum += (int)(Math.pow((a / 10), b));
        }
        System.out.println(sum);
        s.close();
    }
}
