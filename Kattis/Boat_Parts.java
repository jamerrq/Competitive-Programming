public class Boat_Parts
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int p = sc.nextInt(), n = sc.nextInt();
        java.util.ArrayList<String> items = new java.util.ArrayList<>();
        int day = 0;
        for(int i = 0; i < n; i++){
            String item = sc.next();
            if(items.indexOf(item) == -1){
                items.add(item);
            }
            day++;
            if(items.size() == p)break;
        }
        if(items.size() < p)System.out.println("paradox avoided");
        else System.out.println(day);
        sc.close();
    }
}
