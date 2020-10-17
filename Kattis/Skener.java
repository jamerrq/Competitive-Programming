public class Skener
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int r = sc.nextInt(), c = sc.nextInt(), h = sc.nextInt(), w = sc.nextInt();
        String[] lines = new String[r * h];
        int lastIndex = 0;
        for(int i = 0; i < r + c - c; i++){
            String line = sc.next();
            for(int j = 0; j < h; j++){
                lines[lastIndex] = line;
                lastIndex++;
            }
        }
        if(w != 1){
            for(int i = 0; i < lines.length; i++){
                String n = "";
                for(int j = 0; j < lines[i].length(); j++){
                    for(int k = 0; k < w; k++){
                        n += lines[i].charAt(j);
                    }
                }
                lines[i] = n;
            }
        }
        for(String s: lines){
            System.out.println(s);
        }
        sc.close();
    }
}
