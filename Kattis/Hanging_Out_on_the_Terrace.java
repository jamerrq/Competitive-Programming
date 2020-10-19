public class Hanging_Out_on_the_Terrace
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int L = sc.nextInt(), x = sc.nextInt(), terrace = 0, count = 0;
        for(int i = 0; i < x; i++){
            String e = sc.next();
            int p = sc.nextInt();
            if(e.equals("enter")){
                if(terrace + p <= L){
                    terrace += p;
                }else{
                    count++;
                }
            }else{
                terrace -= p;
            }
        }
        System.out.println(count);
        sc.close();
    }
}
