class Odd_Man_Out{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            int c = sc.nextInt();
            int[] cs = new int[c];
            for(int j = 0; j < c; j++){
                cs[j] = sc.nextInt();
            }
            // System.out.println(java.util.Arrays.toString(cs));
            for(int j = 0; j < c; j++){
                int t = 0;
                for(int k = 0; k < c; k++){
                    if(cs[j] == cs[k])t++;
                }
                // System.out.println(cs[j] + " " + t);
                if(t == 1){
                    System.out.println("Case #" + (i + 1) + ": " + cs[j]);
                    break;
                }
            }
        }
        sc.close();
    }
}
