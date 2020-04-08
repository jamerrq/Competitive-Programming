public class Encoded_Message
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            String m = sc.next();
            int s = (int)(Math.sqrt(m.length()));
            char[][] d = new char[s][s];
            int c = 0;
            for(int j = 0; j < s; j++){
                for(int k = 0; k < s; k++){
                    d[d.length - 1 - k][j] = m.charAt(c);
                    c++;
                }
            }
            String dc = "";
            for(char[] p: d){
                for(char r: p){
                    dc += r;
                }
            }
            System.out.println(dc);
        }
    }
}
