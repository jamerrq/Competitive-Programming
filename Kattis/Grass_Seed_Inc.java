public class Grass_Seed_Inc
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        double cost = sc.nextDouble();
        int lawns = sc.nextInt();
        double total = 0;
        for(int i = 0; i < lawns; i++){
            double width = sc.nextDouble(), length = sc.nextDouble();
            double area = width * length;
            total += area * cost;
        }
        System.out.println(total);
        sc.close();
    }
}
