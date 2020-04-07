import java.util.Scanner;
class Autori{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String n = s.next();
        String a = "";
        for(int i = 0; i < n.length(); i++){
            if(i == 0 || n.charAt(i - 1) == '-')a += n.charAt(i);
        }
        System.out.println(a);
    }
}
