public class Estimating_the_Area_of_a_Circle
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        while(true){
            double r = sc.nextDouble();
            double m = sc.nextDouble(), c = sc.nextDouble();
            if(r == 0 && m == 0 && c == 0)break;
            double a = Math.PI * Math.pow(r,2);
            double e = (c / m) * Math.pow(2 * r, 2);
            System.out.println(a + " " + e);
        }
        sc.close();
    }
}
