public class Symmetric_Order
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int set = 1;
        while(true){
            int n = sc.nextInt();
            if(n == 0)break;
            String[] names = new String[n];
            for(int i = 0; i < n / 2; i++){
                names[i] = sc.next();                
                names[n - i - 1] = sc.next();
            }
            if(n % 2 != 0){
                names[n / 2] = sc.next();
            }
            System.out.println("SET " + set);
            for(String s: names){
                System.out.println(s);
            }
            set++;
        }
    }
}
