public class Bus_Numbers
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        int[] bs = new int[n];
        for(int i = 0; i < n; i++){
            bs[i] = sc.nextInt();
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(bs[i] < bs[j]){
                    int temp = bs[i];
                    bs[i] = bs[j];
                    bs[j] = temp;
                }
            }
        }
        String s = "";
        for(int i = 0; i < n; i++){
            String t = bs[i] + "";
            int min = i, max = -1;
            for(int j = i + 1; j < n; j++){
                if(bs[j] - 1 == bs[i]){
                   t += "-" + bs[j];
                   max = j;
                   i++;
                }else{
                    break;
                }
            }
            if(t.indexOf("-") != t.lastIndexOf("-")){
                t = bs[min] + "-" + bs[max];
            }
            if(max - 1 == min){
                t = bs[min] + " " + bs[max];
            }
            s += t + " ";
        }
        System.out.println(s.trim());
        sc.close();
    }
}
