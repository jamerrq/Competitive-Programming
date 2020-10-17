import java.util.Scanner;
import java.util.Arrays;
public class Akcija
{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] bp = new int[n];
        for(int i = 0; i < n; i++)bp[i] = sc.nextInt();
        Arrays.sort(bp);
        for(int i = 0; i < bp.length / 2; i++){int temp = bp[i]; bp[i] = bp[bp.length - 1 - i]; bp[bp.length - 1 - i] = temp;}
        int sum = 0;
        for(int i = bp.length - 1; i >= 0; i--)if(i == 0 || (i + 1) % 3 != 0)sum += bp[i];
        System.out.println(sum);
        sc.close();
    }
}
