import java.util.Scanner;
class Tarifa{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int x = s.nextInt();
        int n = s.nextInt();
        int m = x * n;
        for(int i = 0; i < n; i++)m -= s.nextInt();
        System.out.println(m + x);
    }
}
