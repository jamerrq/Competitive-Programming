public class Reverse_Rot
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        char[] a = new char[28];
        for(int i = 0; i < 26; i++){
            a[i] = (char)(i + 65);
        }
        a[26] = '_';
        a[27] = '.';
        while(true){
            int n = sc.nextInt();
            if(n == 0)break;
            String m = sc.next();
            String r = "";
            for(int i = 0; i < m.length(); i++){
                char c = m.charAt(m.length() - i - 1);
                if(c == '_')c = 26;
                else if(c == '.')c = 27;
                else c -= 65;
                c += n; c %= 28;
                r += a[c];
            }
            System.out.println(r);
        }
        sc.close();
    }
}
