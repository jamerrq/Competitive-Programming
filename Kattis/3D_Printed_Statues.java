public class Printers
{
    static int n;

    static int printers(int printers, int days, int statues){
        if(printers >= statues)return days + 1;
        return printers(printers * 2, days + 1, statues);
    }

    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        n = sc.nextInt();
        System.out.println(printers(1, 0, n));
    }
}
