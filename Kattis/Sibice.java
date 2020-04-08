public class Sibice
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        int w = sc.nextInt(), h = sc.nextInt();
        double maxL = Math.sqrt(Math.pow(w,2) + Math.pow(h,2));
        for(int i = 0; i < n; i++){
            int m = sc.nextInt();
            if(m <= maxL)System.out.println("DA");
            else System.out.println("NE");
        }
    }
}
