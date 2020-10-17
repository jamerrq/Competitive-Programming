public class Detailed_Differences
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            String a = sc.next(), b = sc.next(), c = "";
            for(int j = 0; j < a.length(); j++){
                if(a.charAt(j) == b.charAt(j))c += ".";
                else c += "*";
            }
            System.out.println(a);
            System.out.println(b);
            System.out.println(c);
            System.out.println();
        }
        sc.close();
    }
}
