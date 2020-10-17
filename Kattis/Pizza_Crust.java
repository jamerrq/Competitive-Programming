public class Pizza_Crust
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        double r = sc.nextDouble(), c = sc.nextDouble();
        double ar = Math.PI * Math.pow(r, 2), ac = Math.PI * Math.pow(r - c, 2);
        double percentage = (ac / ar) * 100;
        System.out.println(percentage);
        sc.close();
    }
}
