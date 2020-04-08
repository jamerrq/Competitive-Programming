public class Prva
{
    static boolean less(String a, String b){
        if(a.length() == 0)return true;
        if(b.length() == 0)return false;
        if(a.charAt(0) == b.charAt(0))return less(a.substring(1), b.substring(1));
        if(a.charAt(0) < b.charAt(0))return true;
        return false;
    }
    
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int numRows = sc.nextInt(), numCols = sc.nextInt();
        String[] rows = new String[numRows], cols = new String[numCols];
        for(int i = 0; i < numCols; i++)cols[i] = "";
        String word = "";
        for(int i = 0; i < numRows; i++){
            rows[i] = sc.next();
            for(int j = 0; j < rows[i].length(); j++){
                cols[j] += rows[i].charAt(j);
            }
        }
        for(int i = 0; i < Math.max(numRows, numCols); i++)word += 'z';
        for(String row: rows){
            String[] words = row.split("#");
            for(String w: words){
                if(w.length() > 1 && less(w, word)){
                    word = w;
                }
            }
        }
        for(String col: cols){
            String[] words = col.split("#");
            for(String w: words){
                if(w.length() > 1 && less(w, word)){
                    word = w;
                }
            }
        }
        System.out.println(word);
    }
    // 4 4 luka o#a# kula i#a# : kala
    // 4 4 luka o#a# kula i#as : as
    // 4 5 adaca da##b abb#b abbac : abb
}
