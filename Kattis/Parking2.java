public class Parking2
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int cases = sc.nextInt();
        for(int i = 0; i < cases; i++){
            int numStores = sc.nextInt();
            int[] stores = new int[numStores];
            for(int j = 0; j < numStores; j++){
                stores[j] = sc.nextInt();
            }
            int min = Integer.MAX_VALUE;
            int max = 0;
            for(int j = 0; j < numStores; j++){
                min = Math.min(min, stores[j]);
                max = Math.max(max, stores[j]);
            }
            System.out.println(2 * (max - min));
        }
    }
}
