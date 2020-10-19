public class Ragged_Right
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        java.util.ArrayList<String> lines = new java.util.ArrayList<>();
        int n = 0;
        while(sc.hasNextLine()){
            String line = sc.nextLine();
            if(line.length() > n)n = line.length();
            lines.add(line);
        }
        int measure = 0;
        for(int i = 0; i < lines.size() - 1; i++){
            measure += Math.pow(n - lines.get(i).length(), 2);
        }
        System.out.println(measure);
        sc.close();
    }
}
