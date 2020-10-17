public class Herman
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int r = sc.nextInt();
        System.out.println((Math.PI * Math.pow(r,2)));
        System.out.println((2 * Math.pow(r,2)));
        sc.close();
    }
}
