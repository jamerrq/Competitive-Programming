public class Zamka
{
    static int sum(int n){
        int sum = 0;
        while(n != 0){sum += n % 10; n /= 10;}
        return sum;
    }

    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int L = sc.nextInt(), D = sc.nextInt(), X = sc.nextInt();
        int N = L, M = D;
        for(int i = N; i < D + 1; i++){
            if(sum(i) == X){
                N = i; break;
            }
        }
        for(int i = D; i > N - 1; i--){
            if(sum(i) == X){
                M = i; break;
            }
        }
        System.out.println(N);
        System.out.println(M);
        sc.close();
    }
}
