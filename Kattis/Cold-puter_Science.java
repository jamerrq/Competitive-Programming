public class Cold-puter_Science
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        for(int i = 0; i < n; i++){
            int t = sc.nextInt();
            if(t < 0)sum++;
        }
        System.out.println(sum);
    }
}
