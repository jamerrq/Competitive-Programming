public class Volim
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int k = sc.nextInt(), n = sc.nextInt(), time = 0;
        for(int i = 0; i < n; i++){
            int t = sc.nextInt();
            String a = sc.next();
            time += t;
            if(time >= 210)break;
            else{
                if(a.equals("T")){
                    k++;
                    if(k > 8)k -= 8;
                }
            }
        }
        System.out.println(k);
        sc.close();
    }
}
