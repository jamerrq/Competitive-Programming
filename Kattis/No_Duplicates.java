public class No_Duplicates
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        java.util.ArrayList<String> words = new java.util.ArrayList<>();
        boolean repeated = false;
        while(sc.hasNext()){
            String word = sc.next();
            if(words.indexOf(word) != -1){
                repeated = true;
                break;
            }else{
                words.add(word);
            }
        }
        if(repeated)System.out.println("no"); else System.out.println("yes");
        sc.close();
    }
}
