import java.util.Scanner;
public class Ilya_and_Bank_Account
{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        if(n >= 0){System.out.println(n);}
        else{
            if(n > -11){
                System.out.println(0);
            }else{
                String v = String.valueOf(n);
                int max = n;
                if(Integer.parseInt(v.substring(0, v.length() - 1)) > n){
                    max = Integer.parseInt(v.substring(0, v.length() - 1));
                }
                if(Integer.parseInt(v.substring(0, v.length() - 2)
                    + v.charAt(v.length() - 1)) > max){
                    max = Integer.parseInt(v.substring(0, v.length() - 2)
                    + v.charAt(v.length() - 1));
                }
                System.out.println(max);
            }
        }
        s.close();
    }
}