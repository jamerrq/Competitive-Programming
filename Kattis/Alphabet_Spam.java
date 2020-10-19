public class Alphabet_Spam
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String l = sc.next();
        double lc = 0, uc = 0, sp = 0, sy = 0;
        for(int i = 0; i < l.length(); i++){
            int t = l.charAt(i);
            if(t >= 65 && t <= 90)uc++;
            else if(t >= 97 && t <= 122)lc++;
            else if(t == 95)sp++;
            else sy++;
        }
        System.out.println(sp / l.length());
        System.out.println(lc / l.length());
        System.out.println(uc / l.length());
        System.out.println(sy / l.length());
        sc.close();
    }
}
