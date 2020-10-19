public class Speed_Limit
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        while(true){
            int n = sc.nextInt();
            if(n == -1)break;
            int h = 0, k = 0;
            for(int i = 0; i < n; i++){
                int v = sc.nextInt(), ht = sc.nextInt();
                ht -= h; h += ht;
                k += v * ht;
            }
            System.out.println(k + " miles");
        }
        sc.close();
    }
}
