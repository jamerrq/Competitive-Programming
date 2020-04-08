public class Heart_Rate
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            int b = sc.nextInt();
            double p = sc.nextDouble();
            double min = 60 / (p / (b - 1)), mid = 60 / (p / b), max = 60 / (p / (b + 1));
            System.out.println(min + " " + mid + " " + max);
        }        
    }
}
