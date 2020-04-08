public class The_Amazing_Human_Cannonball
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            double v = sc.nextDouble(), a = sc.nextDouble(), x = sc.nextDouble(), h1 = sc.nextDouble(), h2 = sc.nextDouble();
            double t = x / (v * Math.cos(Math.toRadians(a)));
            double y = v * t * Math.sin(Math.toRadians(a)) - 0.5 * 9.81 * Math.pow(t, 2);
            if(y - h1 >= 1 && h2 - y >= 1)System.out.println("Safe");
            else System.out.println("Not Safe");
        }
    }
}
