import java.util.Scanner;

class The_jackpot{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while(true){
            int N = sc.nextInt();
            if(N == 0)break;
            int[] arr = new int[N];
            for(int i = 0; i < N; ++i){
                arr[i] = sc.nextInt();
            }
            int ans = 0;
            for(int i = 0; i < N; ++i){
                ans = Math.max(ans, ans + arr[i]);
            }
            System.out.print(ans);
        }
    }
}
