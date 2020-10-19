import java.util.Scanner;
public class Sum_Kind_of_Problem
{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            int a = sc.nextInt();
            int b = sc.nextInt() + a - a;
            int sum1 = 0;
            int sum2 = 0;
            int sum3 = 0;
            for(int j = 1; j <= b; j++){sum1 += j; sum2 += j * 2; sum3 += j * 2 - 1;}
            System.out.println((i + 1) + " " + sum1 + " " + sum3 + " " + sum2);
        }
        sc.close();
    }
}
