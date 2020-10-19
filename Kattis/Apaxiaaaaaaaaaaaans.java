import java.util.Scanner;
class Apaxiaaaaaaaaaaaans{
    static String clean(String s){
        if(s.length() < 2)return s;
        if(s.charAt(0) == s.charAt(1))return clean(s.substring(1));
        return s.charAt(0) + clean(s.substring(1));
    }

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String n = s.next();
        System.out.println(clean(n));
        s.close();
    }
}
