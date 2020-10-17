public class Batter_Up
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        int[] s = new int[n];
        for(int i = 0; i < n; i++){
            s[i] = sc.nextInt();
        }
        int sum = 0;
        for(int i = 0; i < s.length; i++){
            if(s[i] == -1)n--;
            else sum += s[i];
        }
        double average = (double)(sum) / n;
        System.out.println(average);
        sc.close();
    }
}
