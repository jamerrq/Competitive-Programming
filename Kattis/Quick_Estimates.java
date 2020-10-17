public class Quick_Estimates
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            String s = sc.next();
            System.out.println(s.length());
        }
        sc.close();
    }
}
