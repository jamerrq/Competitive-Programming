import java.util.Scanner;
import java.util.ArrayList;
class Ive_Been_Everywhere_Man{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            int c = sc.nextInt();
            ArrayList<String> cities = new ArrayList<>();
            for(int j = 0; j < c; j++){
                String city = sc.next();
                if(!cities.contains(city))cities.add(city);
            }
            System.out.println(cities.size());
        }
        sc.close();
    }
}
