public class DRM_Messages
{
    static String rotate(String s){
        int rotate = 0;
        for(int i = 0; i < s.length(); i++){
            rotate += (s.charAt(i) - 65);
        }
        String r = "";
        for(int i = 0; i < s.length(); i++){
            r += (char)(((s.charAt(i) - 65 + rotate) % 26) + 65);
        }
        return r;
    }
    
    static char rotate(char c, char rotate){
        return (char)(((c - 65 + rotate - 65) % 26) + 65);
    }
    
    static String merge(String a, String b){
        String c = "";
        for(int i = 0; i < a.length(); i++){
            c += rotate(a.charAt(i), b.charAt(i));
        }
        return c;
    }

    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String message = sc.next();
        String a = rotate(message.substring(0,message.length() / 2));
        String b = rotate(message.substring(message.length() / 2));
        System.out.println(merge(a, b));
    }
}
