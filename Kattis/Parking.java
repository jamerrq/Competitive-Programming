public class Parking
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        int[][] times = new int[3][2];
        int max = 1, min = 100;
        for(int i = 0; i < 3; i++)for(int j = 0; j < 2; j++){int time = sc.nextInt(); if(time > max)max = time; if(time < min)min = time; times[i][j] = time;}
        int[] trucks = new int[max - min];
        for(int i = 0; i < 3; i++){
            for(int j = times[i][0]; j < times[i][1]; j++){
                trucks[j - min]++;
            }
        }
        int total = 0;
        for(int i = 0; i < trucks.length; i++){
            if(trucks[i] == 1)total += a;
            else if(trucks[i] == 2)total += b * 2;
            else if(trucks[i] == 3)total += c * 3;
        }
        System.out.println(total);
    }
}
